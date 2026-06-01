---
title: Seven JavaScript Quirks I Wish I’d Known About | Telerik Developer Network
date: '2014-04-24T10:41:43+00:00'
format: link
service: instapaper
tags:
- read
external_url: http://developer.telerik.com/featured/seven-javascript-quirks-i-wish-id-known-about/
---

[Seven JavaScript Quirks I Wish I’d Known About | Telerik Developer Network](http://developer.telerik.com/featured/seven-javascript-quirks-i-wish-id-known-about/)  



![](https://i0.wp.com/developer.telerik.com/wp-content/uploads/2014/04/JavaScript_quirks_header.jpg?w=607)

If you are new to JavaScript or it has only been a minor part of your development effort until recently, you may be feeling frustrated. All languages have their quirks – but the paradigm shift from strongly typed server-side languages to JavaScript can feel especially confusing at times. I’ve been there! A few years ago, when I was thrust into full time JavaScript development, there were *many* things I wish I’d known going into it. In this article, I’ll share a few of these quirks in hopes that I might spare you some of the headaches I endured. This isn’t an exhaustive list – just a sampling – but hopefully it will shed some light on the language as well as show how powerful it can be once you get past these kinds of hurdles.

#### The Quirks We’ll look at:

## 1.) Equality

Coming from C#, I was well familiar with the `==` comparison operator. Value types (& strings) are either equal (have the same value) or they aren’t. Reference types are either equal – as in pointing to the same reference – or NOT. (Let’s just pretend you’re not overloading the `==` operator, or implementing your own `Equals` and `GetHashCode` methods.) I was surprised to learn that JavaScript has *two* equality operators: `==` and `===`. Most of the code I’d initially seen used `==`, so I followed suit and wasn’t aware of what JavaScript was doing for me as I ran code like this:

```
var x = 1;

if(x == "1") {
    console.log("YAY! They're equal!");
}
```

So what dark magic is *this*? How can the *integer* 1 equal the *string* “1”?

In JavaScript, there’s equality (`==`) and then there’s *strict* equality (`===`). The equality comparison operator will coerce the operands to the same type and *then* perform a strict equality comparison. So in the above example, the string “1” is being converted, behind the scenes, to the integer 1, and then compared to our variable `x`.

Strict equality doesn’t coerce the types for you. If the operands aren’t of the same type (as in the integer 1 and string “1”), then they *aren’t* equal:

```
var x = 1;

// with strict equality, the types must be the *same* for it to be true
if(x === "1") {
    console.log("Sadly, I'll never write this to the console");
}

if(x === 1) {
    console.log("YES! Strict Equality FTW.")
}
```

You might already be thinking of the kinds of horrors that could occur when type coercion is done for you – the sort of assumptions that you could make that misrepresent the true nature of the values in your app which lead to difficult-to-find-yet-hiding-in-plain-sight bugs. It’s no surprise, then, that the general rule of thumb recommended by experienced JavaScript developers is to *always use strict equality*.

## 2.) Dot Notation vs Bracket Notation

Depending on what other languages you hail from, you probably weren’t too surprised to see these forms of accessing a property on an object and accessing an element in an array in JavaScript:

```
// getting the "firstName" value from the person object:
var name = person.firstName;

// getting the 3rd element in an array:
var theOneWeWant = myArray[2]; // remember, 0-based index
```

However, did you know it’s possible to use bracket notation to reference object members as well? For example:

```
var name = person["firstName"];
```

Why would this be useful? While you’ll probably use dot notation the majority of the time, there are a few instances where bracket notation makes certain approaches possible that couldn’t be done otherwise. For example, I will often refactor large `switch` statements into a [dispatch table](https://en.wikipedia.org/wiki/Dispatch_table), so that something like this:

```
var doSomething = function(doWhat) {
    switch(doWhat) {
        case "doThisThing":
            // more code...
        break;
        case "doThatThing":
            // more code...
        break;
        case "doThisOtherThing":
            // more code....
        break;
        // additional cases here, etc.
        default:
            // default behavior
        break;
    }
}
```

Can be transformed into something like this:

```
var thingsWeCanDo = {
    doThisThing      : function() { /* behavior */ },
    doThatThing      : function() { /* behavior */ },
    doThisOtherThing : function() { /* behavior */ },
    default          : function() { /* behavior */ }
};

var doSomething = function(doWhat) {
    var thingToDo = thingsWeCanDo.hasOwnProperty(doWhat) ? doWhat : "default"
    thingsWeCanDo[thingToDo]();
}
```

There’s nothing inherently wrong with using a `switch` (and in many cases, if you’re iterating and performance is a huge concern, a `switch` may outperform the dispatch table). However, dispatch tables offer a nice way to organize and extend behavior, and bracket notation makes it possible by allowing you to reference a property dynamically at runtime.

## 3.) Function Context

There have been a number of great blog posts about properly understanding the “`this` context” in JavaScript (and I’ll link to several at the bottom of this post), but it definitely makes my list of “things I wish I’d known” right away. It’s really not difficult to look at code and confidently know what `this` is at any point – you just have to learn a couple of rules. Unfortunately, many explanations I read about it early on just added to my confusion. As a result, I’ve tried to simplify the explanation for developers new to JavaScript.

### First – Start With a Global Assumption

By default, until there’s a reason for the execution context to change, `this` refers to the *global object*. In the browser, that would be the `window` object (or `global` in node.js).

### Second – the Value of `this` in Methods

When you have an object with a member that is a function, invoking that method *from the parent object* makes `this` the parent object. For example:

```
var marty = {
    firstName: "Marty",
    lastName: "McFly",
    timeTravel: function(year) {
        console.log(this.firstName + " " + this.lastName + " is time traveling to " + year);
    }
}

marty.timeTravel(1955);
// Marty McFly is time traveling to 1955
```

You might already know that you can take the `marty` object’s `timeTravel` method and create a new reference to it from another object. This is actually quite a powerful feature of JavaScript – enabling us to apply behavior (functions) to more than one target instance:

```
var doc = {
    firstName: "Emmett",
    lastName: "Brown",
}

doc.timeTravel = marty.timeTravel;
```

So – what happens if we invoke `doc.timeTravel(1885)`?

```
doc.timeTravel(1885);
// Emmett Brown is time traveling to 1885
```

Again – deep dark magic. Well, not really. Remember, when you’re invoking a *method*, the `this` context is the parent object it’s being invoked from. Hold on to your DeLoreans, though, cause it’s about the get heavy.

(Note: I’ve updated this section for clarity and to make some corrections from the original post.)

What happens when we save a reference to the `marty.TimeTravel` method and invoke our saved reference? Let’s look:

```
var getBackInTime = marty.timeTravel;
getBackInTime(2014);
// undefined undefined is time traveling to 2014
```

Why “undefined undefined”?! Why not “Marty McFly”?

Let’s ask an important question: *What’s the parent/owning object when we invoke our `getBackInTime` function?* While the `getBackInTime` function will technically exist on the window, we’re invoking it as a *function*, not a method of an object. When we invoke a function like this – with no owning object – the `this` context will be the global object. [David Shariff](http://davidshariff.com/blog/javascript-this-keyword/) has a great way of describing this:

> Whenever a function is called, we must look at the immediate left side of the brackets / parentheses “()”. If on the left side of the parentheses we can see a reference, then the value of “this” passed to the function call is exactly of which that object belongs to, otherwise it is the global object.

Since `getBackInTime`‘s `this` context is the `window` – which does not have `firstName` and `lastName` properties – that explains why we see “undefined undefined”.

So we know that invoking a function directly – no owning object – results in the `this` context being the global object. But I also said that I knew our `getBackInTime` function would exist on the window. How do I know this? Well, unless I’ve wrapped the `getBackInTime` in a different scope (which we’ll investigate when we discuss immediately-invoked-function-expressions), then any vars I declare get attached to the window. Here’s proof from Chrome’s console:

[![](https://i0.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_1-1024x96.png?resize=607%2C57)](https://i2.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_1.png)

This is the perfect time to talk about one of the main areas that `this` trips up developers: subscribing event handlers.

### Third (really just an extension of #2) – The Value of `this` in Methods When Invoked Asynchronously

So, let’s pretend we want to invoke our `marty.timeTravel` method when someone clicks a button:

```
var flux = document.getElementById("flux-capacitor");
flux.addEventListener("click", marty.timeTravel);
```

With the above code, when the user clicks the button, we’ll see “undefined undefined is time traveling to [object MouseEvent]”. WAT?! Well – the first, and most obvious, issue is that we’re not providing the `year` argument to our `timeTravel` method. Instead, we subscribed the method directly as an event handler, and the `MouseEvent` argument is being passed to the event handler as the first arg. That’s easy to fix, but the real issue is that we’re seeing “undefined undefined” again. Don’t despair – you already know why this is the case (even if you don’t realize it yet). Let’s make a change to our `timeTravel` function to log whatever `this` is to help give us some insight:

```
marty.timeTravel = function(year) {
    console.log(this.firstName + " " + this.lastName + " is time traveling to " + year);
    console.log(this);
};
```

Now – when we click the button, we should see something similar to the following output in our browser console:

[![](https://i0.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_2.png?w=607)](https://i1.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_2.png)

Our second `console.log` shows us the `this` context when the method was invoked – and it’s the actual button element which we subscribed to. Does this surprise you? Just like earlier – when we assigned the `marty.timeTravel` reference to our `getBackInTime` var – a reference to `marty.timeTravel` was saved as our event handler and is being invoked, but not from the “owning” `marty` object. In this case, it’s being invoked asynchronously by the underlying [event emitting](http://en.wikipedia.org/wiki/Event-driven_architecture) implementation of the button element instance.

So – is it possible make `this` what we want it to be? Absolutely! In this case, the solution is deceptively simple. Instead of subscribing `marty.timeTravel` directly as the event handler, we can use an anonymous function as our event handler, and call marty.timeTravel from within it. This also provides the opportunity to fix our issue with the missing `year` parameter.

```
flux.addEventListener("click", function(e) {
    marty.timeTravel(someYearValue); 
});
```

Clicking the button now will result in something similar to this output on the console:

[![](https://i0.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquicks_afjq_3-1024x83.png?resize=607%2C49)](https://i0.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquicks_afjq_3.png)

Success! But why did this work? Think of how we’re invoking the `timeTravel` method. In our first button click example, we subscribed the method reference *itself* as the event handler, so it was not being called from the parent object of `marty`. In the second example, it’s our anonymous function that will have a `this` of the button element, and when we invoke `marty.timeTravel`, we’re calling it from the `marty` parent object, and the `this` will be `marty`.

### Fourth – The Value of `this` Inside Constructor Functions.

When you use a constructor function to create a new instance of an object, the `this` value inside the function is the new object that’s being created. For example:

```
var TimeTraveler = function(fName, lName) {
    this.firstName = fName;
    this.lastName = lName;
    // Constructor functions return the
    // newly created object for us unless
    // we specifically return something else
};

var marty = new TimeTraveler("Marty", "McFly");
console.log(marty.firstName + " " + marty.lastName);
// Marty McFly
```
### Using Call, Apply & Bind

You might already suspect, given the above examples, that there might be some language-level features that would allow us to invoke a function and tell it at runtime what `this` should be. You’d be right. The `call` and `apply` methods that exist on the `Function` prototype both allow us to invoke a function and pass in a `this` value.

`call`‘s method signature takes the `this` arg, followed by the parameters the function being invoked would take as separate arguments:

```
someFn.call(this, arg1, arg2, arg3);
```

`apply` takes `this` as the first arg, followed by an array of the remaining arguments:

```
someFn.apply(this, [arg1, arg2, arg3]);
```

Our `doc` and `marty` instances can time travel on their own, but [Einstein](http://backtothefuture.wikia.com/wiki/Einstein) needed their help to time travel. So let’s add a method to our `doc` instance from earlier (the one we copied the `timeTravel` method to), so that `doc` can cause an `einstein` instance to travel in time:

```
doc.timeTravelFor = function(instance, year) {
    this.timeTravel.call(instance, year);
    // alternate syntax if you used apply would be
    // this.timeTravel.apply(instance, [year]);
};
```

Now it’s possible to send Einstein on his way:

```
var einstein = {
    firstName: "Einstein", 
    lastName: "(the dog)"
};
doc.timeTravelFor(einstein, 1985);
// Einstein (the dog) is time traveling to 1985
```

I know this is a contrived example, but it’s enough to give you a glimpse of the power of applying functions to other objects.

There’s still one other possibility we haven’t explored. Let’s give our `marty` instance a `goHome` method that’s simply a shortcut to calling `this.timeTravel(1985)`:

```
marty.goHome = function() {
    this.timeTravel(1985);
}
```

However, we know that if we subscribe `marty.goHome` as the event handler to our button’s click event, that `this` will be the button – and unfortunately buttons don’t have a `timeTravel` method. We could use our approach from earlier – where an anonymous function was the event handler, and it invoked the method on the `marty` instance – but we have another option, the `bind` function:

```
flux.addEventListener("click", marty.goHome.bind(marty));
```

The `bind` function actually returns a *new* function, with the `this` value of the new function set to what you provide as the argument. If you’re supporting older browsers (less than IE9, for example), then you’ll need to [shim the `bind` function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) (or, if you’re using jQuery, you can use `$.proxy`; both underscore & lodash provide `_.bind`).

> One important thing to remember is that if you use `bind` on a *prototype* method, it creates an instance-level method, which bypasses the advantages of having methods on the prototype. It’s not *wrong*, just something to be aware of. I write more about this particular issue [here](http://freshbrewedcode.com/jimcowart/2013/02/12/getting-into-context-binds/).

## 4.) Function Expressions vs Function Declarations

There are two main ways you will typically see functions defined in JavaScript (though ES6 will introduce [another](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions_and_function_scope#The_arrow_function_expression_(.3D))): function declarations and function expressions.

Function Declarations do not require a `var` keyword. In fact, as [Angus Croll says](http://javascriptweblog.wordpress.com/2010/07/06/function-declarations-vs-function-expressions/): *“It’s helpful to think of them as siblings of Variable Declarations.”* For example:

```
function timeTravel(year) {
    console.log(this.firstName + " " + this.lastName + " is time traveling to " + year);
}
```

The function name `timeTravel` in the above example is visible not only inside the scope it was declared, but inside the function itself as well (this is especially useful for recursive function calls). Function declarations are, by nature, *named functions*. In other words, the above function’s `name` property is `timeTravel`.

Function Expressions define a function and assign it to a variable. They typically look like this:

```
var someFn = function() {
    console.log("I like to express myself...");
};
```

It’s possible to name function expressions as well – though, unlike function declarations, a named function expression’s name is only accessible *inside* its scope:

```
var someFn = function iHazName() {
    console.log("I like to express myself...");
    if(needsMoreExpressing) {
        iHazName(); // the function's name can be used here
    }
};

// you can call someFn() here, but not iHazName()
someFn();
```
> Discussing function expressions and declarations wouldn’t be complete without at least mentioning “hoisting” – where function and variable declarations are moved to the top of the containing scope by the interpreter. We’re not going to cover hoisting here, but be sure to read two great explanations by [Ben Cherry](http://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html) and [Angus Croll](http://javascriptweblog.wordpress.com/2010/07/06/function-declarations-vs-function-expressions/).

## 5.) Named vs Anonymous Functions

Based on what we’ve just discussed, you might have guessed that an “anonymous” function is a function without a name. Most JavaScript developers would quickly recognize the second argument below as an anonymous function:

```
someElement.addEventListener("click", function(e) {
    // I'm anonymous!
});
```

However, it’s also true that our `marty.timeTravel` method is anonymous as well:

```
var marty = {
    firstName: "Marty",
    lastName: "McFly",
    timeTravel: function(year) {
        console.log(this.firstName + " " + this.lastName + " is time traveling to " + year);
    }
}
```

Since function declarations must have a name, only function *expressions* can be anonymous.

## 6.) Immediately Invoked Function Expressions

And since we’re talking about function expressions, one thing I wish I’d known right away: the Immediately Invoked Function Expression (IIFE). There are a number of good posts on IIFEs (I’ll list a few at the end), but in a nutshell, it’s a function expression that is not assigned to a variable to be executed later, it’s executed *immediately*. It might help to see this take shape in a browser console.

### First – let’s start with just entering a function expression – but not assigning it – and see what happens:

[![](https://i2.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_4.png?w=607)](https://i2.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_4.png)

That’s not valid JavaScript syntax – it’s a function declaration missing its name. However, to make it an expression, we just need to surround it with parentheses:

[![](https://i1.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_6.png?w=607)](https://i2.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_6.png) [![](https://i2.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_5.png?w=607)](https://i2.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_5.png)

Making this an expression immediately returns our anonymous function to the console (remember, we’re not assigning it, but since it’s an expression we get its value back). So – we have the “function expression” part of “immediately invoked function expression”. To get the “immediately invoked” aspect, we call what the expression returns by adding another set of parentheses after the expression (just like we’d invoke any other function):

[![](https://i1.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_6.png?w=607)](https://i2.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_6.png)

“But wait, Jim! I think I’ve seen this before with the invocation parentheses *inside* the expression parentheses”. Indeed you probably have – it’s perfectly legal syntax (and is well known to be Douglas Crockford’s preferred syntax):

[![](https://i0.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_7.png?w=607)](https://i1.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_7.png)

Either approach on where to put the invocation parentheses is usable, however I highly recommend reading [one of the best explanations ever](https://github.com/airbnb/javascript/issues/21#issuecomment-10203921) on why & when it could matter.

Ok, great – now we know *what* an IIFE *is* – why is it useful?

It helps us control *scope* – an essential part of any JavaScript endeavor! The `marty` instance we’ve looked at earlier was created in the *global* scope. This means that the window (assuming we’re in a browser), will have a `marty` property. If we write all of our JavaScript code this way, we’ll quickly end up with a metric ton of vars declared in the global scope, polluting the window with our app’s code. Even in the best case scenarios, it’s bad practice to leak that many details into the global scope, but what happens when someone names a variable the same name as an *already existing* property on the window? It gets overwritten!

For example, if your favorite “Amelia Earhart” fan site declares a `navigator` variable in the global scope, this is a before and after look at what happens:

[![](https://i0.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_8-1024x222.png?resize=607%2C132)](https://i2.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_8.png)

OOPS!

Obviously – polluting the global scope is **bad**. JavaScript utilizes *function scope* (not block scope, if you’re coming from C# or Java, this is important!), so the way to keep our code from polluting the global scope is to create a *new* scope, and we can use an IIFE to do this since its contents will be inside its own function scope. In the example below, I’m showing you the `window.navigator` value in the console, and then I create an IIFE to wrap the behavior and data specific to Amelia Earhart. This IIFE happens to return an object that will serve as our “application namespace”. Inside the IIFE I declare a `navigator` variable to show that it will *not* overwrite the window.navigator value.

[![](https://i1.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_9-1024x450.png?resize=607%2C267)](https://i0.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_9.png)

As an added bonus, the IIFE we created above is the beginnings of a in JavaScript. I’ll include some links at the end so you can explore module patterns further.

## 7.) The `typeof` Operator and `Object.prototype.toString`

Eventually, you’ll probably find yourself in a situation where you need to inspect the type of a value passed into a function, or something similar. The `typeof` operator might seem the obvious choice, however, it’s not terribly helpful. For example, what happens when we call `typeof` on an object, an array, a string and a regular expression?

[![](https://i2.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_10.png?w=607)](https://i1.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_10.png)

Well – at least we can tell our strings apart from objects, arrays and regular expressions, right? Thankfully, we can take a different approach to get more accurate information about type we’re inspecting. We’ll use the `Object.prototype.toString` function and apply our knowledge of the `call` method from earlier:

[![](https://i2.wp.com/developer.telerik.com/wp-content/uploads/2014/04/jsquirks_afjq_11.png?w=607)](https://i2.wp.com/tdn.azurewebsites.net/wp-content/uploads/2014/04/jsquirks_afjq_11.png)

Why are we using the `toString` on `Object.prototype`? Because it’s possible for 3rd party libraries, as well as your own code, to override the `toString` method with an instance method. By going to the `Object.prototype`, we can force the original `toString` behavior on an instance.

If you know what `typeof` will return and you don’t need to check beyond what it will give you (for example, you just need to know if something is a string or not), then using `typeof` is perfectly fine. However, if you need to tell arrays from objects, regexes from objects, etc., use `Object.prototype.toString`.

## Where to Go Next

I’ve benefitted tremendously from the insights of other JavaScript developers, so please check these links out and give these people a pat on the back for teaching the rest of us!

* Axel Rauschmayer’s great post on [When is it OK to use == in JavaScript?](http://www.2ality.com/2011/12/strict-equality-exemptions.html) (hint: *never*)
* [Fixing the typeof Operator](http://javascriptweblog.wordpress.com/2011/08/08/fixing-the-javascript-typeof-operator/) by Angus Croll
* [Airbnb Github Issue comment](https://github.com/airbnb/javascript/issues/21#issuecomment-10203921) that’s the single best explanation on IIFE parens placement
* [Function Declarations vs. Function Expressions](http://javascriptweblog.wordpress.com/2010/07/06/function-declarations-vs-function-expressions/) – by Angus Croll
* [Getting Into Context Binds](http://freshbrewedcode.com/jimcowart/2013/02/12/getting-into-context-binds/) by yours truly
* [Immediately-Invoked Function Expression (IIFE)](http://benalman.com/news/2010/11/immediately-invoked-function-expression/) by Ben Alman
* [Learning JavaScript Design Patterns](http://addyosmani.com/resources/essentialjsdesignpatterns/book/) by Addy Osmani
* [Understanding the “this” keyword in JavaScript](http://unschooled.org/2012/03/understanding-javascript-this/) by Nicholas Bergson-Shilcock
* [MDN – Function.prototype.bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
* [MDN – Function.prototype.apply](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
* [MDN – Function.prototype.call](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
* [Named function expressions demystified](http://kangax.github.io/nfe/) by Juriy “kangax” Zaytsev
* [Basic JavaScript for the impatient programmer](http://www.2ality.com/2013/06/basic-javascript.html) by Axel Rauschmayer
* [JavaScript Scoping and Hoisting](http://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html) by Ben Cherry
* [JavaScript’s ‘this’ Keyword](http://davidshariff.com/blog/javascript-this-keyword/) by David Shariff
* [What is the Execution Context & Stack in JavaScript?](http://davidshariff.com/blog/what-is-the-execution-context-in-javascript/) by David Shariff

[![](https://i1.wp.com/developer.telerik.com/wp-content/uploads/2014/04/BuildFree_Blog_banner.jpeg?w=607)](http://www.telerik.com/campaigns/kendo-ui-build-free?utm_campaign=kui-build-free&utm_medium=social+media&utm_source=TDN)
"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[3283],{96151:function(e,t,r){r.d(t,{T:function(){return n},y:function(){return i}});var n=function(e){requestAnimationFrame((function(){return setTimeout(e,0)}))},i=function(){return new Promise((function(e){n(e)}))}},67498:function(e,t,r){var n,i,o,a,s,l,c,u,f=r(7599),d=r(26767),p=r(5701),h=r(17717),m=r(48399),y=r(47501),v=r(18457),g=r(96151),b=/^((?!chrome|android).)*safari/i.test(navigator.userAgent);function w(e){return w="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},w(e)}function k(e,t){return t||(t=e.slice(0)),Object.freeze(Object.defineProperties(e,{raw:{value:Object.freeze(t)}}))}function E(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function P(e,t){return P=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e},P(e,t)}function x(e){var t=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var r,n=I(e);if(t){var i=I(this).constructor;r=Reflect.construct(n,arguments,i)}else r=n.apply(this,arguments);return _(this,r)}}function _(e,t){if(t&&("object"===w(t)||"function"==typeof t))return t;if(void 0!==t)throw new TypeError("Derived constructors may only return object or undefined");return O(e)}function O(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function S(){S=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(n){t.forEach((function(t){var i=t.placement;if(t.kind===n&&("static"===i||"prototype"===i)){var o="static"===i?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var n=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===n?void 0:n.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],n=[],i={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,i)}),this),e.forEach((function(e){if(!j(e))return r.push(e);var t=this.decorateElement(e,i);r.push(t.element),r.push.apply(r,t.extras),n.push.apply(n,t.finishers)}),this),!t)return{elements:r,finishers:n};var o=this.decorateConstructor(r,t);return n.push.apply(n,o.finishers),o.finishers=n,o},addElementPlacement:function(e,t,r){var n=t[e.placement];if(!r&&-1!==n.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");n.push(e.key)},decorateElement:function(e,t){for(var r=[],n=[],i=e.decorators,o=i.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,i[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&n.push(l.finisher);var c=l.extras;if(c){for(var u=0;u<c.length;u++)this.addElementPlacement(c[u],t);r.push.apply(r,c)}}return{element:e,finishers:n,extras:r}},decorateConstructor:function(e,t){for(var r=[],n=t.length-1;n>=0;n--){var i=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[n])(i)||i);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return R(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?R(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=z(e.key),n=String(e.placement);if("static"!==n&&"prototype"!==n&&"own"!==n)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+n+'"');var i=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:n,descriptor:Object.assign({},i)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:T(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=T(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var n=(0,t[r])(e);if(void 0!==n){if("function"!=typeof n)throw new TypeError("Finishers must return a constructor.");e=n}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function C(e){var t,r=z(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var n={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(n.decorators=e.decorators),"field"===e.kind&&(n.initializer=e.value),n}function A(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function j(e){return e.decorators&&e.decorators.length}function D(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function T(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function z(e){var t=function(e,t){if("object"!==w(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==w(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===w(t)?t:String(t)}function R(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function N(e,t,r){return N="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var n=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=I(e)););return e}(e,t);if(n){var i=Object.getOwnPropertyDescriptor(n,t);return i.get?i.get.call(r):i.value}},N(e,t,r||e)}function I(e){return I=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},I(e)}var M=function(e,t,r){var n=function(e,t,r){return 100*(e-t)/(r-t)}(function(e,t,r){return isNaN(e)||isNaN(t)||isNaN(r)?0:e>r?r:e<t?t:e}(e,t,r),t,r);return 180*n/100};!function(e,t,r,n){var i=S();if(n)for(var o=0;o<n.length;o++)i=n[o](i);var a=t((function(e){i.initializeInstanceElements(e,s.elements)}),r),s=i.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},n=0;n<e.length;n++){var i,o=e[n];if("method"===o.kind&&(i=t.find(r)))if(D(o.descriptor)||D(i.descriptor)){if(j(o)||j(i))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");i.descriptor=o.descriptor}else{if(j(o)){if(j(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");i.decorators=o.decorators}A(o,i)}else t.push(o)}return t}(a.d.map(C)),e);i.initializeClassElements(a.F,s.elements),i.runClassFinishers(a.F,s.finishers)}([(0,d.M)("ha-gauge")],(function(e,t){var r=function(t){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&P(e,t)}(n,t);var r=x(n);function n(){var t;E(this,n);for(var i=arguments.length,o=new Array(i),a=0;a<i;a++)o[a]=arguments[a];return t=r.call.apply(r,[this].concat(o)),e(O(t)),t}return n}(t);return{F:r,d:[{kind:"field",decorators:[(0,p.C)({type:Number})],key:"min",value:function(){return 0}},{kind:"field",decorators:[(0,p.C)({type:Number})],key:"max",value:function(){return 100}},{kind:"field",decorators:[(0,p.C)({type:Number})],key:"value",value:function(){return 0}},{kind:"field",decorators:[(0,p.C)({type:String})],key:"valueText",value:void 0},{kind:"field",decorators:[(0,p.C)()],key:"locale",value:void 0},{kind:"field",decorators:[(0,p.C)({type:Boolean})],key:"needle",value:void 0},{kind:"field",decorators:[(0,p.C)()],key:"levels",value:void 0},{kind:"field",decorators:[(0,p.C)()],key:"label",value:function(){return""}},{kind:"field",decorators:[(0,h.S)()],key:"_angle",value:function(){return 0}},{kind:"field",decorators:[(0,h.S)()],key:"_updated",value:function(){return!1}},{kind:"method",key:"firstUpdated",value:function(e){var t=this;N(I(r.prototype),"firstUpdated",this).call(this,e),(0,g.T)((function(){t._updated=!0,t._angle=M(t.value,t.min,t.max),t._rescale_svg()}))}},{kind:"method",key:"updated",value:function(e){N(I(r.prototype),"updated",this).call(this,e),this._updated&&e.has("value")&&(this._angle=M(this.value,this.min,this.max),this._rescale_svg())}},{kind:"method",key:"render",value:function(){var e=this;return(0,f.YP)(n||(n=k(['\n      <svg viewBox="0 0 100 50" class="gauge">\n        ',"\n\n        ","\n        ","\n        ",'\n        </path>\n      </svg>\n      <svg class="text">\n        <text class="value-text">\n          '," ","\n        </text>\n      </svg>"])),this.needle&&this.levels?"":(0,f.YP)(i||(i=k(['<path\n          class="dial"\n          d="M 10 50 A 40 40 0 0 1 90 50"\n        ></path>']))),this.levels?this.levels.sort((function(e,t){return e.level-t.level})).map((function(t,r){var n;if(0===r&&t.level!==e.min){var i=M(e.min,e.min,e.max);n=(0,f.YP)(o||(o=k(['<path\n                        stroke="var(--info-color)"\n                        class="level"\n                        d="M\n                          ',"\n                          ",'\n                         A 40 40 0 0 1 90 50\n                        "\n                      ></path>'])),50-40*Math.cos(i*Math.PI/180),50-40*Math.sin(i*Math.PI/180))}var s=M(t.level,e.min,e.max);return(0,f.YP)(a||(a=k(["",'<path\n                      stroke="','"\n                      class="level"\n                      d="M\n                        ',"\n                        ",'\n                       A 40 40 0 0 1 90 50\n                      "\n                    ></path>'])),n,t.stroke,50-40*Math.cos(s*Math.PI/180),50-40*Math.sin(s*Math.PI/180))})):"",this.needle?(0,f.YP)(s||(s=k(['<path\n                class="needle"\n                d="M 25 47.5 L 2.5 50 L 25 52.5 z"\n                style=',"\n                transform=","\n              >\n              "])),(0,m.o)(b?void 0:(0,y.V)({transform:"rotate(".concat(this._angle,"deg)")})),(0,m.o)(b?"rotate(".concat(this._angle," 50 50)"):void 0)):(0,f.YP)(l||(l=k(['<path\n                class="value"\n                d="M 90 50.001 A 40 40 0 0 1 10 50"\n                style=',"\n                transform=","\n              >"])),(0,m.o)(b?void 0:(0,y.V)({transform:"rotate(".concat(this._angle,"deg)")})),(0,m.o)(b?"rotate(".concat(this._angle," 50 50)"):void 0)),b?(0,f.YP)(c||(c=k(['<animateTransform\n                attributeName="transform"\n                type="rotate"\n                from="0 50 50"\n                to="',' 50 50"\n                dur="1s"\n              />'])),this._angle):"",this.valueText||(0,v.u)(this.value,this.locale),this.label)}},{kind:"method",key:"_rescale_svg",value:function(){var e=this.shadowRoot.querySelector(".text"),t=e.querySelector("text").getBBox();e.setAttribute("viewBox","".concat(t.x," ").concat(t.y," ").concat(t.width," ").concat(t.height))}},{kind:"get",static:!0,key:"styles",value:function(){return(0,f.iv)(u||(u=k(["\n      :host {\n        position: relative;\n      }\n      .dial {\n        fill: none;\n        stroke: var(--primary-background-color);\n        stroke-width: 15;\n      }\n      .value {\n        fill: none;\n        stroke-width: 15;\n        stroke: var(--gauge-color);\n        transform-origin: 50% 100%;\n        transition: all 1s ease 0s;\n      }\n      .needle {\n        fill: var(--primary-text-color);\n        transform-origin: 50% 100%;\n        transition: all 1s ease 0s;\n      }\n      .level {\n        fill: none;\n        stroke-width: 15;\n      }\n      .gauge {\n        display: block;\n      }\n      .text {\n        position: absolute;\n        max-height: 40%;\n        max-width: 55%;\n        left: 50%;\n        bottom: -6%;\n        transform: translate(-50%, 0%);\n      }\n      .value-text {\n        font-size: 50px;\n        fill: var(--primary-text-color);\n        text-anchor: middle;\n      }\n    "])))}}]}}),f.oi)},43283:function(e,t,r){r.r(t),r.d(t,{severityMap:function(){return U}});var n,i,o,a,s,l,c=r(7599),u=r(26767),f=r(5701),d=r(17717),p=r(47501),h=r(62877),m=r(47181),y=r(91741),v=r(84627),g=(r(22098),r(67498),r(56007)),b=r(15688),w=r(53658),k=r(75502);function E(e){return E="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},E(e)}function P(e,t){return t||(t=e.slice(0)),Object.freeze(Object.defineProperties(e,{raw:{value:Object.freeze(t)}}))}function x(e,t,r,n,i,o,a){try{var s=e[o](a),l=s.value}catch(c){return void r(c)}s.done?t(l):Promise.resolve(l).then(n,i)}function _(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function O(e,t){return O=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e},O(e,t)}function S(e){var t=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var r,n=Y(e);if(t){var i=Y(this).constructor;r=Reflect.construct(n,arguments,i)}else r=n.apply(this,arguments);return C(this,r)}}function C(e,t){if(t&&("object"===E(t)||"function"==typeof t))return t;if(void 0!==t)throw new TypeError("Derived constructors may only return object or undefined");return A(e)}function A(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function j(){j=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(n){t.forEach((function(t){var i=t.placement;if(t.kind===n&&("static"===i||"prototype"===i)){var o="static"===i?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var n=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===n?void 0:n.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],n=[],i={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,i)}),this),e.forEach((function(e){if(!z(e))return r.push(e);var t=this.decorateElement(e,i);r.push(t.element),r.push.apply(r,t.extras),n.push.apply(n,t.finishers)}),this),!t)return{elements:r,finishers:n};var o=this.decorateConstructor(r,t);return n.push.apply(n,o.finishers),o.finishers=n,o},addElementPlacement:function(e,t,r){var n=t[e.placement];if(!r&&-1!==n.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");n.push(e.key)},decorateElement:function(e,t){for(var r=[],n=[],i=e.decorators,o=i.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,i[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&n.push(l.finisher);var c=l.extras;if(c){for(var u=0;u<c.length;u++)this.addElementPlacement(c[u],t);r.push.apply(r,c)}}return{element:e,finishers:n,extras:r}},decorateConstructor:function(e,t){for(var r=[],n=t.length-1;n>=0;n--){var i=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[n])(i)||i);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||M(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=I(e.key),n=String(e.placement);if("static"!==n&&"prototype"!==n&&"own"!==n)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+n+'"');var i=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:n,descriptor:Object.assign({},i)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:N(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=N(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var n=(0,t[r])(e);if(void 0!==n){if("function"!=typeof n)throw new TypeError("Finishers must return a constructor.");e=n}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function D(e){var t,r=I(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var n={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(n.decorators=e.decorators),"field"===e.kind&&(n.initializer=e.value),n}function T(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function z(e){return e.decorators&&e.decorators.length}function R(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function N(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function I(e){var t=function(e,t){if("object"!==E(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==E(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===E(t)?t:String(t)}function M(e,t){if(e){if("string"==typeof e)return F(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?F(e,t):void 0}}function F(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function B(e,t,r){return B="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var n=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=Y(e)););return e}(e,t);if(n){var i=Object.getOwnPropertyDescriptor(n,t);return i.get?i.get.call(r):i.value}},B(e,t,r||e)}function Y(e){return Y=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},Y(e)}var U={red:"var(--error-color)",green:"var(--success-color)",yellow:"var(--warning-color)",normal:"var(--info-color)"};!function(e,t,r,n){var i=j();if(n)for(var o=0;o<n.length;o++)i=n[o](i);var a=t((function(e){i.initializeInstanceElements(e,s.elements)}),r),s=i.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},n=0;n<e.length;n++){var i,o=e[n];if("method"===o.kind&&(i=t.find(r)))if(R(o.descriptor)||R(i.descriptor)){if(z(o)||z(i))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");i.descriptor=o.descriptor}else{if(z(o)){if(z(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");i.decorators=o.decorators}T(o,i)}else t.push(o)}return t}(a.d.map(D)),e);i.initializeClassElements(a.F,s.elements),i.runClassFinishers(a.F,s.finishers)}([(0,u.M)("hui-gauge-card")],(function(e,t){var u,E,C=function(t){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&O(e,t)}(n,t);var r=S(n);function n(){var t;_(this,n);for(var i=arguments.length,o=new Array(i),a=0;a<i;a++)o[a]=arguments[a];return t=r.call.apply(r,[this].concat(o)),e(A(t)),t}return n}(t);return{F:C,d:[{kind:"method",static:!0,key:"getConfigElement",value:(u=regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Promise.all([r.e(5009),r.e(8161),r.e(2955),r.e(4409),r.e(8055),r.e(9505),r.e(3098),r.e(6087),r.e(6588),r.e(4535),r.e(6902),r.e(7345)]).then(r.bind(r,97345));case 2:return e.abrupt("return",document.createElement("hui-gauge-card-editor"));case 3:case"end":return e.stop()}}),e)})),E=function(){var e=this,t=arguments;return new Promise((function(r,n){var i=u.apply(e,t);function o(e){x(i,r,n,o,a,"next",e)}function a(e){x(i,r,n,o,a,"throw",e)}o(void 0)}))},function(){return E.apply(this,arguments)})},{kind:"method",static:!0,key:"getStubConfig",value:function(e,t,r){return{type:"gauge",entity:(0,b.j)(e,1,t,r,["counter","input_number","number","sensor"],(function(e){return!isNaN(Number(e.state))}))[0]||""}}},{kind:"field",decorators:[(0,f.C)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.S)()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 4}},{kind:"method",key:"setConfig",value:function(e){if(!e.entity)throw new Error("Entity must be specified");if(!(0,v.T)(e.entity))throw new Error("Invalid entity");this._config=Object.assign({min:0,max:100},e)}},{kind:"method",key:"render",value:function(){var e,t;if(!this._config||!this.hass)return(0,c.dy)(n||(n=P([""])));var r=this.hass.states[this._config.entity];if(!r)return(0,c.dy)(i||(i=P(["\n        <hui-warning>\n          ","\n        </hui-warning>\n      "])),(0,k.i)(this.hass,this._config.entity));var l=Number(r.state);if(r.state===g.nZ)return(0,c.dy)(o||(o=P(["\n        <hui-warning\n          >","</hui-warning\n        >\n      "])),this.hass.localize("ui.panel.lovelace.warning.entity_unavailable","entity",this._config.entity));if(isNaN(l))return(0,c.dy)(a||(a=P(["\n        <hui-warning\n          >","</hui-warning\n        >\n      "])),this.hass.localize("ui.panel.lovelace.warning.entity_non_numeric","entity",this._config.entity));var u=null!==(e=this._config.name)&&void 0!==e?e:(0,y.C)(r);return(0,c.dy)(s||(s=P(["\n      <ha-card @click=",' tabindex="0">\n        <ha-gauge\n          .min=',"\n          .max=","\n          .value=","\n          .locale=","\n          .label=","\n          style=","\n          .needle=","\n          .levels=",'\n        ></ha-gauge>\n        <div class="name" .title=',">","</div>\n      </ha-card>\n    "])),this._handleClick,this._config.min,this._config.max,r.state,this.hass.locale,this._config.unit||(null===(t=this.hass)||void 0===t?void 0:t.states[this._config.entity].attributes.unit_of_measurement)||"",(0,p.V)({"--gauge-color":this._computeSeverity(l)}),this._config.needle,this._config.needle?this._severityLevels():void 0,u,u)}},{kind:"method",key:"shouldUpdate",value:function(e){return(0,w.G)(this,e)}},{kind:"method",key:"updated",value:function(e){if(B(Y(C.prototype),"updated",this).call(this,e),this._config&&this.hass){var t=e.get("hass"),r=e.get("_config");t&&r&&t.themes===this.hass.themes&&r.theme===this._config.theme||(0,h.R)(this,this.hass.themes,this._config.theme)}}},{kind:"method",key:"_computeSeverity",value:function(e){if(!this._config.needle){var t=this._config.severity;if(!t)return U.normal;var r,n=Object.keys(t).map((function(e){return[e,t[e]]})),i=function(e,t){var r="undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(!r){if(Array.isArray(e)||(r=M(e))||t&&e&&"number"==typeof e.length){r&&(e=r);var n=0,i=function(){};return{s:i,n:function(){return n>=e.length?{done:!0}:{done:!1,value:e[n++]}},e:function(e){throw e},f:i}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var o,a=!0,s=!1;return{s:function(){r=r.call(e)},n:function(){var e=r.next();return a=e.done,e},e:function(e){s=!0,o=e},f:function(){try{a||null==r.return||r.return()}finally{if(s)throw o}}}}(n);try{for(i.s();!(r=i.n()).done;){var o=r.value;if(null==U[o[0]]||isNaN(o[1]))return U.normal}}catch(a){i.e(a)}finally{i.f()}return n.sort((function(e,t){return e[1]-t[1]})),e>=n[0][1]&&e<n[1][1]?U[n[0][0]]:e>=n[1][1]&&e<n[2][1]?U[n[1][0]]:e>=n[2][1]?U[n[2][0]]:U.normal}}},{kind:"method",key:"_severityLevels",value:function(){var e=this._config.severity;return e?Object.keys(e).map((function(t){return{level:e[t],stroke:U[t]}})):[{level:0,stroke:U.normal}]}},{kind:"method",key:"_handleClick",value:function(){(0,m.B)(this,"hass-more-info",{entityId:this._config.entity})}},{kind:"get",static:!0,key:"styles",value:function(){return(0,c.iv)(l||(l=P(["\n      ha-card {\n        cursor: pointer;\n        height: 100%;\n        overflow: hidden;\n        padding: 16px;\n        display: flex;\n        align-items: center;\n        justify-content: center;\n        flex-direction: column;\n        box-sizing: border-box;\n      }\n\n      ha-card:focus {\n        outline: none;\n        background: var(--divider-color);\n      }\n\n      ha-gauge {\n        width: 100%;\n        max-width: 250px;\n      }\n\n      .name {\n        text-align: center;\n        line-height: initial;\n        color: var(--primary-text-color);\n        width: 100%;\n        font-size: 15px;\n        margin-top: 8px;\n      }\n    "])))}}]}}),c.oi)}}]);
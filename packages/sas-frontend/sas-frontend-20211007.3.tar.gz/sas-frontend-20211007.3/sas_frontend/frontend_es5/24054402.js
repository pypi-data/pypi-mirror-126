/*! For license information please see 24054402.js.LICENSE.txt */
"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[453],{39841:function(n,t,e){e(94604),e(65660);var o,r,i,a=e(9672),l=e(87156),s=e(50856),u=e(44181);(0,a.k)({_template:(0,s.d)(o||(r=['\n    <style>\n      :host {\n        display: block;\n        /**\n         * Force app-header-layout to have its own stacking context so that its parent can\n         * control the stacking of it relative to other elements (e.g. app-drawer-layout).\n         * This could be done using `isolation: isolate`, but that\'s not well supported\n         * across browsers.\n         */\n        position: relative;\n        z-index: 0;\n      }\n\n      #wrapper ::slotted([slot=header]) {\n        @apply --layout-fixed-top;\n        z-index: 1;\n      }\n\n      #wrapper.initializing ::slotted([slot=header]) {\n        position: relative;\n      }\n\n      :host([has-scrolling-region]) {\n        height: 100%;\n      }\n\n      :host([has-scrolling-region]) #wrapper ::slotted([slot=header]) {\n        position: absolute;\n      }\n\n      :host([has-scrolling-region]) #wrapper.initializing ::slotted([slot=header]) {\n        position: relative;\n      }\n\n      :host([has-scrolling-region]) #wrapper #contentContainer {\n        @apply --layout-fit;\n        overflow-y: auto;\n        -webkit-overflow-scrolling: touch;\n      }\n\n      :host([has-scrolling-region]) #wrapper.initializing #contentContainer {\n        position: relative;\n      }\n\n      :host([fullbleed]) {\n        @apply --layout-vertical;\n        @apply --layout-fit;\n      }\n\n      :host([fullbleed]) #wrapper,\n      :host([fullbleed]) #wrapper #contentContainer {\n        @apply --layout-vertical;\n        @apply --layout-flex;\n      }\n\n      #contentContainer {\n        /* Create a stacking context here so that all children appear below the header. */\n        position: relative;\n        z-index: 0;\n      }\n\n      @media print {\n        :host([has-scrolling-region]) #wrapper #contentContainer {\n          overflow-y: visible;\n        }\n      }\n\n    </style>\n\n    <div id="wrapper" class="initializing">\n      <slot id="headerSlot" name="header"></slot>\n\n      <div id="contentContainer">\n        <slot></slot>\n      </div>\n    </div>\n'],i=['\n    <style>\n      :host {\n        display: block;\n        /**\n         * Force app-header-layout to have its own stacking context so that its parent can\n         * control the stacking of it relative to other elements (e.g. app-drawer-layout).\n         * This could be done using \\`isolation: isolate\\`, but that\'s not well supported\n         * across browsers.\n         */\n        position: relative;\n        z-index: 0;\n      }\n\n      #wrapper ::slotted([slot=header]) {\n        @apply --layout-fixed-top;\n        z-index: 1;\n      }\n\n      #wrapper.initializing ::slotted([slot=header]) {\n        position: relative;\n      }\n\n      :host([has-scrolling-region]) {\n        height: 100%;\n      }\n\n      :host([has-scrolling-region]) #wrapper ::slotted([slot=header]) {\n        position: absolute;\n      }\n\n      :host([has-scrolling-region]) #wrapper.initializing ::slotted([slot=header]) {\n        position: relative;\n      }\n\n      :host([has-scrolling-region]) #wrapper #contentContainer {\n        @apply --layout-fit;\n        overflow-y: auto;\n        -webkit-overflow-scrolling: touch;\n      }\n\n      :host([has-scrolling-region]) #wrapper.initializing #contentContainer {\n        position: relative;\n      }\n\n      :host([fullbleed]) {\n        @apply --layout-vertical;\n        @apply --layout-fit;\n      }\n\n      :host([fullbleed]) #wrapper,\n      :host([fullbleed]) #wrapper #contentContainer {\n        @apply --layout-vertical;\n        @apply --layout-flex;\n      }\n\n      #contentContainer {\n        /* Create a stacking context here so that all children appear below the header. */\n        position: relative;\n        z-index: 0;\n      }\n\n      @media print {\n        :host([has-scrolling-region]) #wrapper #contentContainer {\n          overflow-y: visible;\n        }\n      }\n\n    </style>\n\n    <div id="wrapper" class="initializing">\n      <slot id="headerSlot" name="header"></slot>\n\n      <div id="contentContainer">\n        <slot></slot>\n      </div>\n    </div>\n'],i||(i=r.slice(0)),o=Object.freeze(Object.defineProperties(r,{raw:{value:Object.freeze(i)}})))),is:"app-header-layout",behaviors:[u.Y],properties:{hasScrollingRegion:{type:Boolean,value:!1,reflectToAttribute:!0}},observers:["resetLayout(isAttached, hasScrollingRegion)"],get header(){return(0,l.vz)(this.$.headerSlot).getDistributedNodes()[0]},_updateLayoutStates:function(){var n=this.header;if(this.isAttached&&n){this.$.wrapper.classList.remove("initializing"),n.scrollTarget=this.hasScrollingRegion?this.$.contentContainer:this.ownerDocument.documentElement;var t=n.offsetHeight;this.hasScrollingRegion?(n.style.left="",n.style.right=""):requestAnimationFrame(function(){var t=this.getBoundingClientRect(),e=document.documentElement.clientWidth-t.right;n.style.left=t.left+"px",n.style.right=e+"px"}.bind(this));var e=this.$.contentContainer.style;n.fixed&&!n.condenses&&this.hasScrollingRegion?(e.marginTop=t+"px",e.paddingTop=""):(e.paddingTop=t+"px",e.marginTop="")}}})},23682:function(n,t,e){function o(n,t){if(t.length<n)throw new TypeError(n+" argument"+(n>1?"s":"")+" required, but only "+t.length+" present")}e.d(t,{Z:function(){return o}})},90394:function(n,t,e){function o(n){if(null===n||!0===n||!1===n)return NaN;var t=Number(n);return isNaN(t)?t:t<0?Math.ceil(t):Math.floor(t)}e.d(t,{Z:function(){return o}})},79021:function(n,t,e){e.d(t,{Z:function(){return a}});var o=e(90394),r=e(34327),i=e(23682);function a(n,t){(0,i.Z)(2,arguments);var e=(0,r.Z)(n),a=(0,o.Z)(t);return isNaN(a)?new Date(NaN):a?(e.setDate(e.getDate()+a),e):e}},32182:function(n,t,e){e.d(t,{Z:function(){return a}});var o=e(90394),r=e(34327),i=e(23682);function a(n,t){(0,i.Z)(2,arguments);var e=(0,r.Z)(n),a=(0,o.Z)(t);if(isNaN(a))return new Date(NaN);if(!a)return e;var l=e.getDate(),s=new Date(e.getTime());s.setMonth(e.getMonth()+a+1,0);var u=s.getDate();return l>=u?s:(e.setFullYear(s.getFullYear(),s.getMonth(),l),e)}},70390:function(n,t,e){e.d(t,{Z:function(){return r}});var o=e(93752);function r(){return(0,o.Z)(Date.now())}},47538:function(n,t,e){function o(){var n=new Date,t=n.getFullYear(),e=n.getMonth(),o=n.getDate(),r=new Date(0);return r.setFullYear(t,e,o-1),r.setHours(23,59,59,999),r}e.d(t,{Z:function(){return o}})},82045:function(n,t,e){e.d(t,{Z:function(){return i}});var o=e(34327),r=e(23682);function i(n,t){(0,r.Z)(2,arguments);var e=(0,o.Z)(n).getTime(),i=(0,o.Z)(t.start).getTime(),a=(0,o.Z)(t.end).getTime();if(!(i<=a))throw new RangeError("Invalid interval");return e>=i&&e<=a}},59429:function(n,t,e){e.d(t,{Z:function(){return i}});var o=e(34327),r=e(23682);function i(n){(0,r.Z)(1,arguments);var t=(0,o.Z)(n);return t.setHours(0,0,0,0),t}},13250:function(n,t,e){e.d(t,{Z:function(){return i}});var o=e(34327),r=e(23682);function i(n){(0,r.Z)(1,arguments);var t=(0,o.Z)(n);return t.setDate(1),t.setHours(0,0,0,0),t}},27088:function(n,t,e){e.d(t,{Z:function(){return r}});var o=e(59429);function r(){return(0,o.Z)(Date.now())}},83008:function(n,t,e){function o(){var n=new Date,t=n.getFullYear(),e=n.getMonth(),o=n.getDate(),r=new Date(0);return r.setFullYear(t,e,o-1),r.setHours(0,0,0,0),r}e.d(t,{Z:function(){return o}})},34327:function(n,t,e){e.d(t,{Z:function(){return i}});var o=e(23682);function r(n){return r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(n){return typeof n}:function(n){return n&&"function"==typeof Symbol&&n.constructor===Symbol&&n!==Symbol.prototype?"symbol":typeof n},r(n)}function i(n){(0,o.Z)(1,arguments);var t=Object.prototype.toString.call(n);return n instanceof Date||"object"===r(n)&&"[object Date]"===t?new Date(n.getTime()):"number"==typeof n||"[object Number]"===t?new Date(n):("string"!=typeof n&&"[object String]"!==t||"undefined"==typeof console||(console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://git.io/fjule"),console.warn((new Error).stack)),new Date(NaN))}}}]);
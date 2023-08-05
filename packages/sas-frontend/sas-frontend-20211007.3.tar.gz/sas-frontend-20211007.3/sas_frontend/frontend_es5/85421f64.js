/*! For license information please see 85421f64.js.LICENSE.txt */
"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[5487],{35487:function(e,t,r){r.d(t,{Y:function(){return z}});var n,o=r(87480),i=r(32207),a=r(72774),c={ROOT:"mdc-form-field"},l={LABEL_SELECTOR:".mdc-form-field > label"},f=function(e){function t(r){var n=e.call(this,(0,o.__assign)((0,o.__assign)({},t.defaultAdapter),r))||this;return n.click=function(){n.handleClick()},n}return(0,o.__extends)(t,e),Object.defineProperty(t,"cssClasses",{get:function(){return c},enumerable:!1,configurable:!0}),Object.defineProperty(t,"strings",{get:function(){return l},enumerable:!1,configurable:!0}),Object.defineProperty(t,"defaultAdapter",{get:function(){return{activateInputRipple:function(){},deactivateInputRipple:function(){},deregisterInteractionHandler:function(){},registerInteractionHandler:function(){}}},enumerable:!1,configurable:!0}),t.prototype.init=function(){this.adapter.registerInteractionHandler("click",this.click)},t.prototype.destroy=function(){this.adapter.deregisterInteractionHandler("click",this.click)},t.prototype.handleClick=function(){var e=this;this.adapter.activateInputRipple(),requestAnimationFrame((function(){e.adapter.deactivateInputRipple()}))},t}(a.K),u=r(78220),d=r(18601),s=r(14114),p=r(59685);function m(e){return m="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},m(e)}function y(e,t,r,n,o,i,a){try{var c=e[i](a),l=c.value}catch(f){return void r(f)}c.done?t(l):Promise.resolve(l).then(n,o)}function h(e){return function(){var t=this,r=arguments;return new Promise((function(n,o){var i=e.apply(t,r);function a(e){y(i,n,o,a,c,"next",e)}function c(e){y(i,n,o,a,c,"throw",e)}a(void 0)}))}}function b(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function g(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function v(e,t){return v=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e},v(e,t)}function w(e){var t=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var r,n=x(e);if(t){var o=x(this).constructor;r=Reflect.construct(n,arguments,o)}else r=n.apply(this,arguments);return _(this,r)}}function _(e,t){if(t&&("object"===m(t)||"function"==typeof t))return t;if(void 0!==t)throw new TypeError("Derived constructors may only return object or undefined");return function(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e)}function x(e){return x=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},x(e)}var O,R=function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&v(e,t)}(c,e);var t,r,o,a=w(c);function c(){var e;return b(this,c),(e=a.apply(this,arguments)).alignEnd=!1,e.spaceBetween=!1,e.nowrap=!1,e.label="",e.mdcFoundationClass=f,e}return t=c,r=[{key:"createAdapter",value:function(){var e,t,r=this;return{registerInteractionHandler:function(e,t){r.labelEl.addEventListener(e,t)},deregisterInteractionHandler:function(e,t){r.labelEl.removeEventListener(e,t)},activateInputRipple:(t=h(regeneratorRuntime.mark((function e(){var t,n;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!((t=r.input)instanceof d.Wg)){e.next=6;break}return e.next=4,t.ripple;case 4:(n=e.sent)&&n.startPress();case 6:case"end":return e.stop()}}),e)}))),function(){return t.apply(this,arguments)}),deactivateInputRipple:(e=h(regeneratorRuntime.mark((function e(){var t,n;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!((t=r.input)instanceof d.Wg)){e.next=6;break}return e.next=4,t.ripple;case 4:(n=e.sent)&&n.endPress();case 6:case"end":return e.stop()}}),e)}))),function(){return e.apply(this,arguments)})}}},{key:"input",get:function(){var e,t;return null!==(t=null===(e=this.slottedInputs)||void 0===e?void 0:e[0])&&void 0!==t?t:null}},{key:"render",value:function(){var e={"mdc-form-field--align-end":this.alignEnd,"mdc-form-field--space-between":this.spaceBetween,"mdc-form-field--nowrap":this.nowrap};return(0,i.dy)(n||(n=function(e,t){return t||(t=e.slice(0)),Object.freeze(Object.defineProperties(e,{raw:{value:Object.freeze(t)}}))}(['\n      <div class="mdc-form-field ','">\n        <slot></slot>\n        <label class="mdc-label"\n               @click="','">',"</label>\n      </div>"])),(0,p.$)(e),this._labelClick,this.label)}},{key:"_labelClick",value:function(){var e=this.input;e&&(e.focus(),e.click())}}],r&&g(t.prototype,r),o&&g(t,o),c}(u.H);(0,o.__decorate)([(0,i.Cb)({type:Boolean})],R.prototype,"alignEnd",void 0),(0,o.__decorate)([(0,i.Cb)({type:Boolean})],R.prototype,"spaceBetween",void 0),(0,o.__decorate)([(0,i.Cb)({type:Boolean})],R.prototype,"nowrap",void 0),(0,o.__decorate)([(0,i.Cb)({type:String}),(0,s.P)(function(){var e=h(regeneratorRuntime.mark((function e(t){var r;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:null===(r=this.input)||void 0===r||r.setAttribute("aria-label",t);case 1:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}())],R.prototype,"label",void 0),(0,o.__decorate)([(0,i.IO)(".mdc-form-field")],R.prototype,"mdcRoot",void 0),(0,o.__decorate)([(0,i.vZ)("",!0,"*")],R.prototype,"slottedInputs",void 0),(0,o.__decorate)([(0,i.IO)("label")],R.prototype,"labelEl",void 0);var k=(0,i.iv)(O||(O=function(e,t){return t||(t=e.slice(0)),Object.freeze(Object.defineProperties(e,{raw:{value:Object.freeze(t)}}))}([".mdc-form-field{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:0.875rem;font-size:var(--mdc-typography-body2-font-size, 0.875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight, 400);letter-spacing:0.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, 0.0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform, inherit);color:rgba(0, 0, 0, 0.87);color:var(--mdc-theme-text-primary-on-background, rgba(0, 0, 0, 0.87));display:inline-flex;align-items:center;vertical-align:middle}.mdc-form-field>label{margin-left:0;margin-right:auto;padding-left:4px;padding-right:0;order:0}[dir=rtl] .mdc-form-field>label,.mdc-form-field>label[dir=rtl]{margin-left:auto;margin-right:0}[dir=rtl] .mdc-form-field>label,.mdc-form-field>label[dir=rtl]{padding-left:0;padding-right:4px}.mdc-form-field--nowrap>label{text-overflow:ellipsis;overflow:hidden;white-space:nowrap}.mdc-form-field--align-end>label{margin-left:auto;margin-right:0;padding-left:0;padding-right:4px;order:-1}[dir=rtl] .mdc-form-field--align-end>label,.mdc-form-field--align-end>label[dir=rtl]{margin-left:0;margin-right:auto}[dir=rtl] .mdc-form-field--align-end>label,.mdc-form-field--align-end>label[dir=rtl]{padding-left:4px;padding-right:0}.mdc-form-field--space-between{justify-content:space-between}.mdc-form-field--space-between>label{margin:0}[dir=rtl] .mdc-form-field--space-between>label,.mdc-form-field--space-between>label[dir=rtl]{margin:0}:host{display:inline-flex}.mdc-form-field{width:100%}::slotted(*){-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:0.875rem;font-size:var(--mdc-typography-body2-font-size, 0.875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight, 400);letter-spacing:0.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, 0.0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform, inherit);color:rgba(0, 0, 0, 0.87);color:var(--mdc-theme-text-primary-on-background, rgba(0, 0, 0, 0.87))}::slotted(mwc-switch){margin-right:10px}[dir=rtl] ::slotted(mwc-switch),::slotted(mwc-switch[dir=rtl]){margin-left:10px}"])));function j(e){return j="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},j(e)}function P(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function E(e,t){return E=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e},E(e,t)}function I(e){var t=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var r,n=S(e);if(t){var o=S(this).constructor;r=Reflect.construct(n,arguments,o)}else r=n.apply(this,arguments);return C(this,r)}}function C(e,t){if(t&&("object"===j(t)||"function"==typeof t))return t;if(void 0!==t)throw new TypeError("Derived constructors may only return object or undefined");return function(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e)}function S(e){return S=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},S(e)}var z=function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&E(e,t)}(r,e);var t=I(r);function r(){return P(this,r),t.apply(this,arguments)}return r}(R);z.styles=[k],z=(0,o.__decorate)([(0,i.Mo)("mwc-formfield")],z)}}]);
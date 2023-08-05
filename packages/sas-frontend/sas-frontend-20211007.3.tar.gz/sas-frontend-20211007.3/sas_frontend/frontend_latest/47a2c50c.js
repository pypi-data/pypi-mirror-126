"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[25534],{51621:(e,t,l)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.GetOperands=void 0;var a=l(71160);t.GetOperands=function(e){a.invariant("string"==typeof e,"GetOperands should have been called with a string");var t=a.ToNumber(e);a.invariant(isFinite(t),"n should be finite");var l,r,i,n=e.indexOf("."),o="";-1===n?(l=t,r=0,i=0):(l=e.slice(0,n),o=e.slice(n,e.length),r=a.ToNumber(o),i=o.length);var u,s,c=Math.abs(a.ToNumber(l));if(0!==r){var f=o.replace(/0+$/,"");u=f.length,s=a.ToNumber(f)}else u=0,s=0;return{Number:t,IntegerDigits:c,NumberOfFractionDigits:i,NumberOfFractionDigitsWithoutTrailing:u,FractionDigits:r,FractionDigitsWithoutTrailing:s}}},75533:(e,t,l)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.InitializePluralRules=void 0;var a=l(71160),r=l(17595);t.InitializePluralRules=function(e,t,l,i){var n=i.availableLocales,o=i.relevantExtensionKeys,u=i.localeData,s=i.getDefaultLocale,c=i.getInternalSlots,f=a.CanonicalizeLocaleList(t),d=Object.create(null),p=a.CoerceOptionsToObject(l),v=c(e);v.initializedPluralRules=!0;var b=a.GetOption(p,"localeMatcher","string",["best fit","lookup"],"best fit");d.localeMatcher=b,v.type=a.GetOption(p,"type","string",["cardinal","ordinal"],"cardinal"),a.SetNumberFormatDigitOptions(v,p,0,3,"standard");var g=r.ResolveLocale(n,f,d,o,u,s);return v.locale=g.locale,e}},93087:(e,t,l)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.ResolvePlural=void 0;var a=l(71160),r=l(51621);t.ResolvePlural=function(e,t,l){var i=l.getInternalSlots,n=l.PluralRuleSelect,o=i(e);if(a.invariant("Object"===a.Type(o),"pl has to be an object"),a.invariant("initializedPluralRules"in o,"pluralrules must be initialized"),a.invariant("Number"===a.Type(t),"n must be a number"),!isFinite(t))return"other";var u=o.locale,s=o.type,c=a.FormatNumericToString(o,t).formattedString;return n(u,s,t,r.GetOperands(c))}},68441:(e,t)=>{Object.defineProperty(t,"__esModule",{value:!0});var l=new WeakMap;t.default=function(e){var t=l.get(e);return t||(t=Object.create(null),l.set(e,t)),t}},78643:(e,t,l)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.PluralRules=void 0;var a=l(87480),r=l(71160),i=l(75533),n=l(93087),o=a.__importDefault(l(68441));function u(e,t){if(!(e instanceof c))throw new TypeError("Method Intl.PluralRules.prototype."+t+" called on incompatible receiver "+String(e))}function s(e,t,l,a){var r=a.IntegerDigits,i=a.NumberOfFractionDigits,n=a.FractionDigits;return c.localeData[e].fn(i?r+"."+n:r,"ordinal"===t)}var c=function(){function e(t,l){if(!(this&&this instanceof e?this.constructor:void 0))throw new TypeError("Intl.PluralRules must be called with 'new'");return i.InitializePluralRules(this,t,l,{availableLocales:e.availableLocales,relevantExtensionKeys:e.relevantExtensionKeys,localeData:e.localeData,getDefaultLocale:e.getDefaultLocale,getInternalSlots:o.default})}return e.prototype.resolvedOptions=function(){u(this,"resolvedOptions");var t=Object.create(null),l=o.default(this);return t.locale=l.locale,t.type=l.type,["minimumIntegerDigits","minimumFractionDigits","maximumFractionDigits","minimumSignificantDigits","maximumSignificantDigits"].forEach((function(e){var a=l[e];void 0!==a&&(t[e]=a)})),t.pluralCategories=a.__spreadArray([],e.localeData[t.locale].categories[t.type]),t},e.prototype.select=function(e){u(this,"select");var t=r.ToNumber(e);return n.ResolvePlural(this,t,{getInternalSlots:o.default,PluralRuleSelect:s})},e.prototype.toString=function(){return"[object Intl.PluralRules]"},e.supportedLocalesOf=function(t,l){return r.SupportedLocales(e.availableLocales,r.CanonicalizeLocaleList(t),l)},e.__addLocaleData=function(){for(var t=[],l=0;l<arguments.length;l++)t[l]=arguments[l];for(var a=0,r=t;a<r.length;a++){var i=r[a],n=i.data,o=i.locale;e.localeData[o]=n,e.availableLocales.add(o),e.__defaultLocale||(e.__defaultLocale=o)}},e.getDefaultLocale=function(){return e.__defaultLocale},e.localeData={},e.availableLocales=new Set,e.__defaultLocale="",e.relevantExtensionKeys=[],e.polyfilled=!0,e}();t.PluralRules=c;try{"undefined"!=typeof Symbol&&Object.defineProperty(c.prototype,Symbol.toStringTag,{value:"Intl.PluralRules",writable:!1,enumerable:!1,configurable:!0});try{Object.defineProperty(c,"length",{value:0,writable:!1,enumerable:!1,configurable:!0})}catch(e){}Object.defineProperty(c.prototype.constructor,"length",{value:0,writable:!1,enumerable:!1,configurable:!0}),Object.defineProperty(c.supportedLocalesOf,"length",{value:1,writable:!1,enumerable:!1,configurable:!0})}catch(e){}},25534:(e,t,l)=>{Object.defineProperty(t,"__esModule",{value:!0});var a=l(78643);l(27815).shouldPolyfill()&&Object.defineProperty(Intl,"PluralRules",{value:a.PluralRules,writable:!0,enumerable:!1,configurable:!0})},27815:(e,t)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.shouldPolyfill=void 0,t.shouldPolyfill=function(e){return!("PluralRules"in Intl)||"one"===new Intl.PluralRules("en",{minimumFractionDigits:2}).select(1)||!function(e){if(!e)return!0;var t=Array.isArray(e)?e:[e];return Intl.PluralRules.supportedLocalesOf(t).length===t.length}(e)}}}]);
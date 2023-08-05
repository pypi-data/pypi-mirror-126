"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[41360],{23682:(e,t,r)=>{function n(e,t){if(t.length<e)throw new TypeError(e+" argument"+(e>1?"s":"")+" required, but only "+t.length+" present")}r.d(t,{Z:()=>n})},90394:(e,t,r)=>{function n(e){if(null===e||!0===e||!1===e)return NaN;var t=Number(e);return isNaN(t)?t:t<0?Math.ceil(t):Math.floor(t)}r.d(t,{Z:()=>n})},79021:(e,t,r)=>{r.d(t,{Z:()=>s});var n=r(90394),a=r(34327),o=r(23682);function s(e,t){(0,o.Z)(2,arguments);var r=(0,a.Z)(e),s=(0,n.Z)(t);return isNaN(s)?new Date(NaN):s?(r.setDate(r.getDate()+s),r):r}},59699:(e,t,r)=>{r.d(t,{Z:()=>i});var n=r(90394),a=r(39244),o=r(23682),s=36e5;function i(e,t){(0,o.Z)(2,arguments);var r=(0,n.Z)(t);return(0,a.Z)(e,r*s)}},39244:(e,t,r)=>{r.d(t,{Z:()=>s});var n=r(90394),a=r(34327),o=r(23682);function s(e,t){(0,o.Z)(2,arguments);var r=(0,a.Z)(e).getTime(),s=(0,n.Z)(t);return new Date(r+s)}},32182:(e,t,r)=>{r.d(t,{Z:()=>s});var n=r(90394),a=r(34327),o=r(23682);function s(e,t){(0,o.Z)(2,arguments);var r=(0,a.Z)(e),s=(0,n.Z)(t);if(isNaN(s))return new Date(NaN);if(!s)return r;var i=r.getDate(),u=new Date(r.getTime());u.setMonth(r.getMonth()+s+1,0);var c=u.getDate();return i>=c?u:(r.setFullYear(u.getFullYear(),u.getMonth(),i),r)}},93752:(e,t,r)=>{r.d(t,{Z:()=>o});var n=r(34327),a=r(23682);function o(e){(0,a.Z)(1,arguments);var t=(0,n.Z)(e);return t.setHours(23,59,59,999),t}},70390:(e,t,r)=>{r.d(t,{Z:()=>a});var n=r(93752);function a(){return(0,n.Z)(Date.now())}},47538:(e,t,r)=>{function n(){var e=new Date,t=e.getFullYear(),r=e.getMonth(),n=e.getDate(),a=new Date(0);return a.setFullYear(t,r,n-1),a.setHours(23,59,59,999),a}r.d(t,{Z:()=>n})},59429:(e,t,r)=>{r.d(t,{Z:()=>o});var n=r(34327),a=r(23682);function o(e){(0,a.Z)(1,arguments);var t=(0,n.Z)(e);return t.setHours(0,0,0,0),t}},13250:(e,t,r)=>{r.d(t,{Z:()=>o});var n=r(34327),a=r(23682);function o(e){(0,a.Z)(1,arguments);var t=(0,n.Z)(e);return t.setDate(1),t.setHours(0,0,0,0),t}},27088:(e,t,r)=>{r.d(t,{Z:()=>a});var n=r(59429);function a(){return(0,n.Z)(Date.now())}},83008:(e,t,r)=>{function n(){var e=new Date,t=e.getFullYear(),r=e.getMonth(),n=e.getDate(),a=new Date(0);return a.setFullYear(t,r,n-1),a.setHours(0,0,0,0),a}r.d(t,{Z:()=>n})},34327:(e,t,r)=>{r.d(t,{Z:()=>a});var n=r(23682);function a(e){(0,n.Z)(1,arguments);var t=Object.prototype.toString.call(e);return e instanceof Date||"object"==typeof e&&"[object Date]"===t?new Date(e.getTime()):"number"==typeof e||"[object Number]"===t?new Date(e):("string"!=typeof e&&"[object String]"!==t||"undefined"==typeof console||(console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://git.io/fjule"),console.warn((new Error).stack)),new Date(NaN))}},66054:(e,t,r)=>{r.a(e,(async e=>{r.r(t),r.d(t,{EnergyStrategy:()=>o});var n=r(55424),a=e([n]);n=(a.then?await a:a)[0];class o{static async generateView(e){const t=e.hass,a={cards:[]};let o;try{o=await(0,n.ZC)(t)}catch(e){return"not_found"===e.code?(async()=>(await Promise.all([r.e(878),r.e(88369)]).then(r.bind(r,55158)),{type:"panel",cards:[{type:"custom:energy-setup-wizard-card"}]}))():(a.cards.push({type:"markdown",content:`An error occured while fetching your energy preferences: ${e.message}.`}),a)}a.type="sidebar";const s=o.energy_sources.find((e=>"grid"===e.type)),i=s&&s.flow_to.length,u=o.energy_sources.some((e=>"solar"===e.type)),c=o.energy_sources.some((e=>"gas"===e.type));return e.narrow&&a.cards.push({type:"energy-date-selection",collection_key:"energy_dashboard",view_layout:{position:"sidebar"}}),s&&a.cards.push({title:"Energy usage",type:"energy-usage-graph",collection_key:"energy_dashboard"}),u&&a.cards.push({title:"Solar production",type:"energy-solar-graph",collection_key:"energy_dashboard"}),c&&a.cards.push({title:"Gas consumption",type:"energy-gas-graph",collection_key:"energy_dashboard"}),s&&a.cards.push({title:"Energy distribution",type:"energy-distribution",view_layout:{position:"sidebar"},collection_key:"energy_dashboard"}),(s||u)&&a.cards.push({title:"Sources",type:"energy-sources-table",collection_key:"energy_dashboard"}),i&&a.cards.push({type:"energy-grid-neutrality-gauge",view_layout:{position:"sidebar"},collection_key:"energy_dashboard"}),u&&i&&a.cards.push({type:"energy-solar-consumed-gauge",view_layout:{position:"sidebar"},collection_key:"energy_dashboard"}),s&&a.cards.push({type:"energy-carbon-consumed-gauge",view_layout:{position:"sidebar"},collection_key:"energy_dashboard"}),o.device_consumption.length&&a.cards.push({title:"Monitor individual devices",type:"energy-devices-graph",collection_key:"energy_dashboard"}),a}}}))}}]);
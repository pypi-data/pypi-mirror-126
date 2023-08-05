"use strict";(self.webpackChunkrichie_education=self.webpackChunkrichie_education||[]).push([[18323],{35164:function(e,t,n){n.d(t,{vt:function(){return b},tV:function(){return f},Fz:function(){return h},Pq:function(){return p}}),n(32390),n(54883),n(10853),n(35054),n(45007),n(68995),n(73214),n(19701),n(19457),n(54994),n(42900),n(21496);var r=n(89526),o=n(7124),u=n(19898),a=(n(55862),n(1368)),i=n(69701);function c(e,t,n,r,o,u,a){try{var i=e[u](a),c=i.value}catch(e){return void n(e)}i.done?t(c):Promise.resolve(c).then(r,o)}var s=function(){var e,t=(e=regeneratorRuntime.mark((function e(t,n,r){var o,c,s;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,fetch("/api/v1.0/".concat(t,"/autocomplete/?").concat((0,i.stringify)({query:r})),{headers:{"Content-Type":"application/json"}});case 3:o=e.sent,e.next=9;break;case 6:return e.prev=6,e.t0=e.catch(0),e.abrupt("return",(0,u.p)(e.t0));case 9:if(o.ok){e.next=22;break}if(c=new Error("Failed to get list from ".concat(t," autocomplete : ").concat(o.status)),400!==o.status){e.next=20;break}return e.t2=u.p,e.t3=c,e.next=16,o.json();case 16:e.t4=e.sent,e.t1=(0,e.t2)(e.t3,e.t4),e.next=21;break;case 20:e.t1=(0,u.p)(c);case 21:return e.abrupt("return",e.t1);case 22:return e.prev=22,e.next=25,o.json();case 25:s=e.sent,e.next=31;break;case 28:return e.prev=28,e.t5=e.catch(22),e.abrupt("return",(0,u.p)(new Error("Failed to decode JSON in getSuggestionSection "+e.t5)));case 31:return e.abrupt("return",{kind:t,title:n,values:(0,a.Z)(s,3)});case 32:case"end":return e.stop()}}),e,null,[[0,6],[22,28]])})),function(){var t=this,n=arguments;return new Promise((function(r,o){var u=e.apply(t,n);function a(e){c(u,r,o,a,i,"next",e)}function i(e){c(u,r,o,a,i,"throw",e)}a(void 0)}))});return function(e,n,r){return t.apply(this,arguments)}}();function l(e,t,n,r,o,u,a){try{var i=e[u](a),c=i.value}catch(e){return void n(e)}i.done?t(c):Promise.resolve(c).then(r,o)}var f=function(e){return e.title},p=function(e){return r.createElement("span",null,e.title)},v=function(){var e,t=(e=regeneratorRuntime.mark((function e(t,n,r){var o;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!(r.length<3)){e.next=2;break}return e.abrupt("return",n([]));case 2:return e.prev=2,e.t0=Promise,e.t1=Object,e.next=7,t;case 7:return e.t2=e.sent,e.t3=e.t1.values.call(e.t1,e.t2).filter((function(e){return e.is_autocompletable})).map((function(e){return s(e.name,e.human_name,r)})),e.next=11,e.t0.all.call(e.t0,e.t3);case 11:o=e.sent,e.next=17;break;case 14:return e.prev=14,e.t4=e.catch(2),e.abrupt("return",(0,u.p)(e.t4));case 17:n(o.filter((function(e){return!!e.values.length})));case 18:case"end":return e.stop()}}),e,null,[[2,14]])})),function(){var t=this,n=arguments;return new Promise((function(r,o){var u=e.apply(t,n);function a(e){l(u,r,o,a,i,"next",e)}function i(e){l(u,r,o,a,i,"throw",e)}a(void 0)}))});return function(e,n,r){return t.apply(this,arguments)}}(),h=(0,o.Z)(v,200,{maxWait:1e3}),b=function(e,t){var n=Object.values(e).find((function(e){return e.name===t.kind}));return n||(n=Object.values(e).find((function(e){return!!e.base_path&&String(t.id).substr(2).startsWith(e.base_path)}))),n}},18323:function(e,t,n){n.r(t),n.d(t,{default:function(){return S}}),n(32390),n(55862),n(54994),n(54883),n(10853),n(68995),n(26364),n(86632),n(61928),n(45007),n(18821),n(4845),n(39275),n(80044),n(19701),n(80238),n(6208),n(12938),n(35054);var r=n(69701),o=n(89526),u=n(80292),a=n.n(u),i=n(34323),c=n(35164),s=n(63456),l=n(33469),f=n(95418);function p(e){return"courses"===e.kind}var v=n(68919);function h(e,t,n,r,o,u,a){try{var i=e[u](a),c=i.value}catch(e){return void n(e)}i.done?t(c):Promise.resolve(c).then(r,o)}function b(e){return function(){var t=this,n=arguments;return new Promise((function(r,o){var u=e.apply(t,n);function a(e){h(u,r,o,a,i,"next",e)}function i(e){h(u,r,o,a,i,"throw",e)}a(void 0)}))}}function g(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function d(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?g(Object(n),!0).forEach((function(t){m(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):g(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function m(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function y(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=n){var r,o,u=[],a=!0,i=!1;try{for(n=n.call(e);!(a=(r=n.next()).done)&&(u.push(r.value),!t||u.length!==t);a=!0);}catch(e){i=!0,o=e}finally{try{a||null==n.return||n.return()}finally{if(i)throw o}}return u}}(e,t)||function(e,t){if(e){if("string"==typeof e)return w(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?w(e,t):void 0}}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function w(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}var O=(0,i.vU)({searchFieldPlaceholder:{id:"components.RootSearchSuggestField.searchFieldPlaceholder",defaultMessage:[{type:0,value:"Search for courses"}]}}),S=function(e){var t=e.context,n=e.courseSearchPageUrl,u=(0,i.YB)(),h=(0,l.U)(!0),g=y((0,o.useState)(""),2),w=g[0],S=g[1],j=y((0,o.useState)([]),2),x=j[0],P=j[1],k=y((0,o.useState)(!1),2),_=k[0],E=k[1],R=function(){return v.xh.assign("".concat(n,"?").concat((0,r.stringify)(d(d({},f.e_),{},{query:w}))))},C={onChange:function(e,t){var n=t.newValue;S(n)},onKeyDown:function(e){13!==e.keyCode||_||R()},placeholder:u.formatMessage(O.searchFieldPlaceholder),value:w},A=function(){var e=b(regeneratorRuntime.mark((function e(t,o){var u,a;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!p(u=o.suggestion)){e.next=3;break}return e.abrupt("return",v.xh.assign(u.absolute_url));case 3:return e.t0=c.vt,e.next=6,h();case 6:e.t1=e.sent,e.t2=u,a=(0,e.t0)(e.t1,e.t2),v.xh.assign("".concat(n,"?").concat((0,r.stringify)(d(d({},f.e_),{},m({},a.name,u.id)))));case 10:case"end":return e.stop()}}),e)})));return function(t,n){return e.apply(this,arguments)}}();return o.createElement(a(),{getSectionSuggestions:function(e){return e.values},getSuggestionValue:c.tV,inputProps:C,multiSection:!0,onSuggestionsClearRequested:function(){return P([])},onSuggestionsFetchRequested:function(){var e=b(regeneratorRuntime.mark((function e(t){var n;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=t.value,e.t0=c.Fz,e.next=4,h();case 4:return e.t1=e.sent,e.t2=P,e.t3=n,e.abrupt("return",(0,e.t0)(e.t1,e.t2,e.t3));case 8:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),onSuggestionHighlighted:function(e){var t=e.suggestion;return E(!!t)},onSuggestionSelected:A,renderInputComponent:function(e){return o.createElement(s.M,{context:t,inputProps:e,onClick:R})},renderSectionTitle:function(e){return e.title},renderSuggestion:c.Pq,shouldRenderSuggestions:function(e){return e.length>2},suggestions:x})}},63456:function(e,t,n){n.d(t,{M:function(){return a}});var r=n(89526),o=n(34323),u=(0,o.vU)({button:{id:"components.SearchInput.button",defaultMessage:[{type:0,value:"Search"}]}}),a=function(e){var t=e.inputProps,n=e.onClick,a=void 0===n?function(){}:n;return r.createElement("div",{className:"search-input"},r.createElement("input",t),r.createElement("button",{className:"search-input__btn",onClick:a},r.createElement("svg",{"aria-hidden":!0,role:"img",className:"icon search-input__btn__icon"},r.createElement("use",{xlinkHref:"#icon-magnifying-glass"}))," ",r.createElement("span",{className:"offscreen"},r.createElement(o._H,u.button))))}},33469:function(e,t,n){n.d(t,{U:function(){return v}}),n(32390),n(10853),n(35054),n(26364),n(86632),n(61928),n(54883),n(45007),n(68995),n(18821),n(54994),n(4845),n(39275),n(80044),n(19701),n(80238),n(6208),n(12938);var r=n(89526),o=n(3787);function u(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?u(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):u(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function c(e,t,n,r,o,u,a){try{var i=e[u](a),c=i.value}catch(e){return void n(e)}i.done?t(c):Promise.resolve(c).then(r,o)}function s(e){return function(){var t=this,n=arguments;return new Promise((function(r,o){var u=e.apply(t,n);function a(e){c(u,r,o,a,i,"next",e)}function i(e){c(u,r,o,a,i,"throw",e)}a(void 0)}))}}function l(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=n){var r,o,u=[],a=!0,i=!1;try{for(n=n.call(e);!(a=(r=n.next()).done)&&(u.push(r.value),!t||u.length!==t);a=!0);}catch(e){i=!0,o=e}finally{try{a||null==n.return||n.return()}finally{if(i)throw o}}return u}}(e,t)||function(e,t){if(e){if("string"==typeof e)return f(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?f(e,t):void 0}}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function f(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}var p={base_path:null,human_name:"Courses",is_autocompletable:!0,is_searchable:!0,name:"courses",position:99},v=function(){var e=arguments.length>0&&void 0!==arguments[0]&&arguments[0],t=(0,r.useState)(!1),n=l(t,2),u=n[0],i=n[1],c=(0,r.useRef)(null),f=(0,r.useState)((function(){return new Promise((function(e){return c.current=e}))})),v=l(f,1),h=v[0];return(0,o.b)(s(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(!u){t.next=10;break}return t.next=3,fetch("/api/v1.0/filter-definitions/");case 3:if((n=t.sent).ok){t.next=6;break}throw new Error("Failed to get filter definitions.");case 6:return t.next=8,n.json();case 8:r=t.sent,c.current(a(a({},r),e?{courses:p}:{}));case 10:case"end":return t.stop()}}),t)}))),[u]),function(){return i(!0),h}}}}]);
//# sourceMappingURL=18323.e894b2552334d7259027.index.js.map
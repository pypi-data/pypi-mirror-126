"use strict";(self.webpackChunkrichie_education=self.webpackChunkrichie_education||[]).push([[18856],{93389:function(e,t,a){Object.defineProperty(t,"__esModule",{value:!0}),t.InitializeRelativeTimeFormat=void 0;var r=a(61279),n=a(29150),i=/^[a-z0-9]{3,8}(-[a-z0-9]{3,8})*$/i;t.InitializeRelativeTimeFormat=function(e,t,a,o){var l=o.getInternalSlots,u=o.availableLocales,s=o.relevantExtensionKeys,c=o.localeData,f=o.getDefaultLocale,v=l(e);v.initializedRelativeTimeFormat=!0;var d=r.CanonicalizeLocaleList(t),m=Object.create(null),p=r.CoerceOptionsToObject(a),y=r.GetOption(p,"localeMatcher","string",["best fit","lookup"],"best fit");m.localeMatcher=y;var b=r.GetOption(p,"numberingSystem","string",void 0,void 0);if(void 0!==b&&!i.test(b))throw new RangeError("Invalid numbering system "+b);m.nu=b;var h=n.ResolveLocale(u,d,m,s,c,f),g=h.locale,w=h.nu;v.locale=g,v.style=r.GetOption(p,"style","string",["long","narrow","short"],"long"),v.numeric=r.GetOption(p,"numeric","string",["always","auto"],"always");var T=c[h.dataLocale];return r.invariant(!!T,"Missing locale data for "+h.dataLocale),v.fields=T,v.numberFormat=new Intl.NumberFormat(t),v.pluralRules=new Intl.PluralRules(t),v.numberingSystem=w,e}},85852:function(e,t,a){Object.defineProperty(t,"__esModule",{value:!0}),t.MakePartsList=void 0;var r=a(61279);t.MakePartsList=function(e,t,a){for(var n=[],i=0,o=r.PartitionPattern(e);i<o.length;i++){var l=o[i];if("literal"===l.type)n.push({type:"literal",value:l.value});else{r.invariant("0"===l.type,"Malformed pattern "+e);for(var u=0,s=a;u<s.length;u++){var c=s[u];n.push({type:c.type,value:c.value,unit:t})}}}return n}},86334:function(e,t,a){Object.defineProperty(t,"__esModule",{value:!0}),t.PartitionRelativeTimePattern=void 0;var r=a(61279),n=a(85877),i=a(85852);t.PartitionRelativeTimePattern=function(e,t,a,o){var l=o.getInternalSlots;if(r.invariant("Number"===r.Type(t),"value must be number, instead got "+typeof t,TypeError),r.invariant("String"===r.Type(a),"unit must be number, instead got "+typeof t,TypeError),isNaN(t)||!isFinite(t))throw new RangeError("Invalid value "+t);var u=n.SingularRelativeTimeUnit(a),s=l(e),c=s.fields,f=s.style,v=s.numeric,d=s.pluralRules,m=s.numberFormat,p=u;"short"===f?p=u+"-short":"narrow"===f&&(p=u+"-narrow"),p in c||(p=u);var y=c[p];if("auto"===v&&r.ToString(t)in y)return[{type:"literal",value:y[r.ToString(t)]}];var b="future";(r.SameValue(t,-0)||t<0)&&(b="past");var h=y[b],g="function"==typeof m.formatToParts?m.formatToParts(Math.abs(t)):[{type:"literal",value:m.format(Math.abs(t)),unit:a}],w=h[d.select(t)];return i.MakePartsList(w,u,g)}},85877:function(e,t,a){Object.defineProperty(t,"__esModule",{value:!0}),t.SingularRelativeTimeUnit=void 0;var r=a(61279);t.SingularRelativeTimeUnit=function(e){if(r.invariant("String"===r.Type(e),"unit must be a string"),"seconds"===e)return"second";if("minutes"===e)return"minute";if("hours"===e)return"hour";if("days"===e)return"day";if("weeks"===e)return"week";if("months"===e)return"month";if("quarters"===e)return"quarter";if("years"===e)return"year";if("second"!==e&&"minute"!==e&&"hour"!==e&&"day"!==e&&"week"!==e&&"month"!==e&&"quarter"!==e&&"year"!==e)throw new RangeError("invalid unit");return e}},69533:function(e,t){Object.defineProperty(t,"__esModule",{value:!0});var a=new WeakMap;t.default=function(e){var t=a.get(e);return t||(t=Object.create(null),a.set(e,t)),t}},18856:function(e,t,a){Object.defineProperty(t,"__esModule",{value:!0});var r=a(33940),n=a(61279),i=a(93389),o=a(86334),l=r.__importDefault(a(69533)),u=function(){function e(t,a){if(!(this&&this instanceof e?this.constructor:void 0))throw new TypeError("Intl.RelativeTimeFormat must be called with 'new'");return i.InitializeRelativeTimeFormat(this,t,a,{getInternalSlots:l.default,availableLocales:e.availableLocales,relevantExtensionKeys:e.relevantExtensionKeys,localeData:e.localeData,getDefaultLocale:e.getDefaultLocale})}return e.prototype.format=function(e,t){if("object"!=typeof this)throw new TypeError("format was called on a non-object");if(!l.default(this).initializedRelativeTimeFormat)throw new TypeError("format was called on a invalid context");return o.PartitionRelativeTimePattern(this,Number(e),n.ToString(t),{getInternalSlots:l.default}).map((function(e){return e.value})).join("")},e.prototype.formatToParts=function(e,t){if("object"!=typeof this)throw new TypeError("formatToParts was called on a non-object");if(!l.default(this).initializedRelativeTimeFormat)throw new TypeError("formatToParts was called on a invalid context");return o.PartitionRelativeTimePattern(this,Number(e),n.ToString(t),{getInternalSlots:l.default})},e.prototype.resolvedOptions=function(){if("object"!=typeof this)throw new TypeError("resolvedOptions was called on a non-object");var e=l.default(this);if(!e.initializedRelativeTimeFormat)throw new TypeError("resolvedOptions was called on a invalid context");return{locale:e.locale,style:e.style,numeric:e.numeric,numberingSystem:e.numberingSystem}},e.supportedLocalesOf=function(t,a){return n.SupportedLocales(e.availableLocales,n.CanonicalizeLocaleList(t),a)},e.__addLocaleData=function(){for(var t=[],a=0;a<arguments.length;a++)t[a]=arguments[a];for(var r=0,n=t;r<n.length;r++){var i=n[r],o=i.data,l=i.locale,u=new Intl.Locale(l).minimize().toString();e.localeData[l]=e.localeData[u]=o,e.availableLocales.add(u),e.availableLocales.add(l),e.__defaultLocale||(e.__defaultLocale=u)}},e.getDefaultLocale=function(){return e.__defaultLocale},e.localeData={},e.availableLocales=new Set,e.__defaultLocale="",e.relevantExtensionKeys=["nu"],e.polyfilled=!0,e}();t.default=u;try{"undefined"!=typeof Symbol&&Object.defineProperty(u.prototype,Symbol.toStringTag,{value:"Intl.RelativeTimeFormat",writable:!1,enumerable:!1,configurable:!0}),Object.defineProperty(u.prototype.constructor,"length",{value:0,writable:!1,enumerable:!1,configurable:!0}),Object.defineProperty(u.supportedLocalesOf,"length",{value:1,writable:!1,enumerable:!1,configurable:!0})}catch(e){}}}]);
//# sourceMappingURL=18856.e894b2552334d7259027.index.js.map
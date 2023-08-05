(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[11],{2885:function(e,t,r){var n;!function(){"use strict";var o={not_string:/[^s]/,not_bool:/[^t]/,not_type:/[^T]/,not_primitive:/[^v]/,number:/[diefg]/,numeric_arg:/[bcdiefguxX]/,json:/[j]/,not_json:/[^j]/,text:/^[^\x25]+/,modulo:/^\x25{2}/,placeholder:/^\x25(?:([1-9]\d*)\$|\(([^)]+)\))?(\+)?(0|'[^$])?(-)?(\d+)?(?:\.(\d+))?([b-gijostTuvxX])/,key:/^([a-z_][a-z_\d]*)/i,key_access:/^\.([a-z_][a-z_\d]*)/i,index_access:/^\[(\d+)\]/,sign:/^[+-]/};function i(e){return s(u(e),arguments)}function a(e,t){return i.apply(null,[e].concat(t||[]))}function s(e,t){var r,n,a,s,c,u,d,l,p,h=1,f=e.length,g="";for(n=0;n<f;n++)if("string"===typeof e[n])g+=e[n];else if("object"===typeof e[n]){if((s=e[n]).keys)for(r=t[h],a=0;a<s.keys.length;a++){if(void 0==r)throw new Error(i('[sprintf] Cannot access property "%s" of undefined value "%s"',s.keys[a],s.keys[a-1]));r=r[s.keys[a]]}else r=s.param_no?t[s.param_no]:t[h++];if(o.not_type.test(s.type)&&o.not_primitive.test(s.type)&&r instanceof Function&&(r=r()),o.numeric_arg.test(s.type)&&"number"!==typeof r&&isNaN(r))throw new TypeError(i("[sprintf] expecting number but found %T",r));switch(o.number.test(s.type)&&(l=r>=0),s.type){case"b":r=parseInt(r,10).toString(2);break;case"c":r=String.fromCharCode(parseInt(r,10));break;case"d":case"i":r=parseInt(r,10);break;case"j":r=JSON.stringify(r,null,s.width?parseInt(s.width):0);break;case"e":r=s.precision?parseFloat(r).toExponential(s.precision):parseFloat(r).toExponential();break;case"f":r=s.precision?parseFloat(r).toFixed(s.precision):parseFloat(r);break;case"g":r=s.precision?String(Number(r.toPrecision(s.precision))):parseFloat(r);break;case"o":r=(parseInt(r,10)>>>0).toString(8);break;case"s":r=String(r),r=s.precision?r.substring(0,s.precision):r;break;case"t":r=String(!!r),r=s.precision?r.substring(0,s.precision):r;break;case"T":r=Object.prototype.toString.call(r).slice(8,-1).toLowerCase(),r=s.precision?r.substring(0,s.precision):r;break;case"u":r=parseInt(r,10)>>>0;break;case"v":r=r.valueOf(),r=s.precision?r.substring(0,s.precision):r;break;case"x":r=(parseInt(r,10)>>>0).toString(16);break;case"X":r=(parseInt(r,10)>>>0).toString(16).toUpperCase()}o.json.test(s.type)?g+=r:(!o.number.test(s.type)||l&&!s.sign?p="":(p=l?"+":"-",r=r.toString().replace(o.sign,"")),u=s.pad_char?"0"===s.pad_char?"0":s.pad_char.charAt(1):" ",d=s.width-(p+r).length,c=s.width&&d>0?u.repeat(d):"",g+=s.align?p+r+c:"0"===u?p+c+r:c+p+r)}return g}var c=Object.create(null);function u(e){if(c[e])return c[e];for(var t,r=e,n=[],i=0;r;){if(null!==(t=o.text.exec(r)))n.push(t[0]);else if(null!==(t=o.modulo.exec(r)))n.push("%");else{if(null===(t=o.placeholder.exec(r)))throw new SyntaxError("[sprintf] unexpected placeholder");if(t[2]){i|=1;var a=[],s=t[2],u=[];if(null===(u=o.key.exec(s)))throw new SyntaxError("[sprintf] failed to parse named argument key");for(a.push(u[1]);""!==(s=s.substring(u[0].length));)if(null!==(u=o.key_access.exec(s)))a.push(u[1]);else{if(null===(u=o.index_access.exec(s)))throw new SyntaxError("[sprintf] failed to parse named argument key");a.push(u[1])}t[2]=a}else i|=2;if(3===i)throw new Error("[sprintf] mixing positional and named placeholders is not (yet) supported");n.push({placeholder:t[0],param_no:t[1],keys:t[2],sign:t[3],pad_char:t[4],align:t[5],width:t[6],precision:t[7],type:t[8]})}r=r.substring(t[0].length)}return c[e]=n}t.sprintf=i,t.vsprintf=a,"undefined"!==typeof window&&(window.sprintf=i,window.vsprintf=a,void 0===(n=function(){return{sprintf:i,vsprintf:a}}.call(t,r,t,e))||(e.exports=n))}()},2886:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),function(e){e.Right="to right",e.Left="to left",e.Down="to bottom",e.Up="to top"}(t.Direction||(t.Direction={}))},3102:function(e,t,r){"use strict";var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0});var o=n(r(3770));t.Range=o.default;var i=r(3103);t.getTrackBackground=i.getTrackBackground,t.useThumbOverlap=i.useThumbOverlap,t.relativeValue=i.relativeValue;var a=r(2886);t.Direction=a.Direction},3103:function(e,t,r){"use strict";var n=this&&this.__spreadArrays||function(){for(var e=0,t=0,r=arguments.length;t<r;t++)e+=arguments[t].length;var n=Array(e),o=0;for(t=0;t<r;t++)for(var i=arguments[t],a=0,s=i.length;a<s;a++,o++)n[o]=i[a];return n};Object.defineProperty(t,"__esModule",{value:!0});var o=r(0),i=r(2886);function a(e){return e===i.Direction.Up||e===i.Direction.Down}function s(e,t,r){e.style.transform="translate("+t+"px, "+r+"px)"}t.getStepDecimals=function(e){var t=e.toString().split(".")[1];return t?t.length:0},t.isTouchEvent=function(e){return e.touches&&e.touches.length||e.changedTouches&&e.changedTouches.length},t.isStepDivisible=function(e,t,r){var n=(t-e)/r;return parseInt(n.toString(),10)===n},t.normalizeValue=function(e,r,n,o,i,a,s){var c=1e11;if(e=Math.round(e*c)/c,!a){var u=s[r-1],d=s[r+1];if(u&&u>e)return u;if(d&&d<e)return d}if(e>o)return o;if(e<n)return n;var l=Math.floor(e*c-n*c)%Math.floor(i*c),p=Math.floor(e*c-Math.abs(l)),h=0===l?e:p/c,f=Math.abs(l/c)<i/2?h:h+i,g=t.getStepDecimals(i);return parseFloat(f.toFixed(g))},t.relativeValue=function(e,t,r){return(e-t)/(r-t)},t.isVertical=a,t.checkBoundaries=function(e,t,r){if(t>=r)throw new RangeError("min ("+t+") is equal/bigger than max ("+r+")");if(e<t)throw new RangeError("value ("+e+") is smaller than min ("+t+")");if(e>r)throw new RangeError("value ("+e+") is bigger than max ("+r+")")},t.checkInitialOverlap=function(e){if(!(e.length<2)&&!e.slice(1).every((function(t,r){return e[r]<=t})))throw new RangeError("values={["+e+"]} needs to be sorted when allowOverlap={false}")},t.getMargin=function(e){var t=window.getComputedStyle(e);return{top:parseInt(t["margin-top"],10),bottom:parseInt(t["margin-bottom"],10),left:parseInt(t["margin-left"],10),right:parseInt(t["margin-right"],10)}},t.getPaddingAndBorder=function(e){var t=window.getComputedStyle(e);return{top:parseInt(t["padding-top"],10)+parseInt(t["border-top-width"],10),bottom:parseInt(t["padding-bottom"],10)+parseInt(t["border-bottom-width"],10),left:parseInt(t["padding-left"],10)+parseInt(t["border-left-width"],10),right:parseInt(t["padding-right"],10)+parseInt(t["border-right-width"],10)}},t.translateThumbs=function(e,t,r){var n=r?-1:1;e.forEach((function(e,r){return s(e,n*t[r].x,t[r].y)}))},t.getClosestThumbIndex=function(e,t,r,n){for(var o=0,i=u(e[0],t,r,n),a=1;a<e.length;a++){var s=u(e[a],t,r,n);s<i&&(i=s,o=a)}return o},t.translate=s,t.schd=function(e){var t=[],r=null;return function(){for(var n=[],o=0;o<arguments.length;o++)n[o]=arguments[o];t=n,r||(r=requestAnimationFrame((function(){r=null,e.apply(void 0,t)})))}},t.replaceAt=function(e,t,r){var n=e.slice(0);return n[t]=r,n},t.getTrackBackground=function(e){var t=e.values,r=e.colors,n=e.min,o=e.max,a=e.direction,s=void 0===a?i.Direction.Right:a,c=e.rtl,u=void 0!==c&&c;u&&s===i.Direction.Right?s=i.Direction.Left:u&&i.Direction.Left&&(s=i.Direction.Right);var d=t.slice(0).sort((function(e,t){return e-t})).map((function(e){return(e-n)/(o-n)*100})).reduce((function(e,t,n){return e+", "+r[n]+" "+t+"%, "+r[n+1]+" "+t+"%"}),"");return"linear-gradient("+s+", "+r[0]+" 0%"+d+", "+r[r.length-1]+" 100%)"},t.voidFn=function(){},t.assertUnreachable=function(e){throw new Error("Didn't expect to get here")};var c=function(e,t,r,o,i){return void 0===i&&(i=function(e){return e}),Math.ceil(n([e],Array.from(e.children)).reduce((function(e,n){var a=Math.ceil(n.getBoundingClientRect().width);if(n.innerText&&n.innerText.includes(r)&&0===n.childElementCount){var s=n.cloneNode(!0);s.innerHTML=i(t.toFixed(o)),s.style.visibility="hidden",document.body.appendChild(s),a=Math.ceil(s.getBoundingClientRect().width),document.body.removeChild(s)}return a>e?a:e}),e.getBoundingClientRect().width))};function u(e,t,r,n){var o=e.getBoundingClientRect(),i=o.x,s=o.y,c=o.width,u=o.height;return a(n)?Math.abs(r-(s+u/2)):Math.abs(t-(i+c/2))}t.useThumbOverlap=function(e,r,i,a,s,u){void 0===a&&(a=.1),void 0===s&&(s=" - "),void 0===u&&(u=function(e){return e});var d=t.getStepDecimals(a),l=o.useState({}),p=l[0],h=l[1],f=o.useState(u(r[i].toFixed(d))),g=f[0],v=f[1];return o.useEffect((function(){if(e){var t=e.getThumbs();if(t.length<1)return;var o={},a=e.getOffsets(),l=function(e,t,r,o,i,a,s){void 0===s&&(s=function(e){return e});var u=[];return function e(d){var l=c(r[d],o[d],i,a,s),p=t[d].x;t.forEach((function(t,h){var f=t.x,g=c(r[h],o[h],i,a,s);d!==h&&(p>=f&&p<=f+g||p+l>=f&&p+l<=f+g)&&(u.includes(h)||(u.push(d),u.push(h),u=n(u,[d,h]),e(h)))}))}(e),Array.from(new Set(u.sort()))}(i,a,t,r,s,d,u),p=u(r[i].toFixed(d));if(l.length){var f=l.reduce((function(e,t,r,o){return e.length?n(e,[a[o[r]].x]):[a[o[r]].x]}),[]);if(Math.min.apply(Math,f)===a[i].x){var g=[];l.forEach((function(e){g.push(r[e].toFixed(d))})),p=Array.from(new Set(g.sort((function(e,t){return parseFloat(e)-parseFloat(t)})))).map(u).join(s);var m=Math.min.apply(Math,f),b=Math.max.apply(Math,f),y=t[l[f.indexOf(b)]].getBoundingClientRect().width;o.left=Math.abs(m-(b+y))/2+"px",o.transform="translate(-50%, 0)"}else o.visibility="hidden"}v(p),h(o)}}),[e,r]),[g,p]}},3770:function(e,t,r){"use strict";var n=this&&this.__extends||function(){var e=function(t,r){return(e=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var r in t)t.hasOwnProperty(r)&&(e[r]=t[r])})(t,r)};return function(t,r){function n(){this.constructor=t}e(t,r),t.prototype=null===r?Object.create(r):(n.prototype=r.prototype,new n)}}(),o=this&&this.__spreadArrays||function(){for(var e=0,t=0,r=arguments.length;t<r;t++)e+=arguments[t].length;var n=Array(e),o=0;for(t=0;t<r;t++)for(var i=arguments[t],a=0,s=i.length;a<s;a++,o++)n[o]=i[a];return n},i=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var r in e)Object.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t.default=e,t};Object.defineProperty(t,"__esModule",{value:!0});var a=i(r(0)),s=r(3103),c=r(2886),u=["ArrowRight","ArrowUp","k","PageUp"],d=["ArrowLeft","ArrowDown","j","PageDown"],l=function(e){function t(t){var r=e.call(this,t)||this;r.trackRef=a.createRef(),r.thumbRefs=[],r.markRefs=[],r.state={draggedTrackPos:[-1,-1],draggedThumbIndex:-1,thumbZIndexes:new Array(r.props.values.length).fill(0).map((function(e,t){return t})),isChanged:!1,markOffsets:[]},r.getOffsets=function(){var e=r.props,t=e.direction,n=e.values,o=e.min,i=e.max,a=r.trackRef.current,u=a.getBoundingClientRect(),d=s.getPaddingAndBorder(a);return r.getThumbs().map((function(e,r){var a={x:0,y:0},l=e.getBoundingClientRect(),p=s.getMargin(e);switch(t){case c.Direction.Right:return a.x=-1*(p.left+d.left),a.y=-1*((l.height-u.height)/2+d.top),a.x+=u.width*s.relativeValue(n[r],o,i)-l.width/2,a;case c.Direction.Left:return a.x=-1*(p.right+d.right),a.y=-1*((l.height-u.height)/2+d.top),a.x+=u.width-u.width*s.relativeValue(n[r],o,i)-l.width/2,a;case c.Direction.Up:return a.x=-1*((l.width-u.width)/2+p.left+d.left),a.y=-d.left,a.y+=u.height-u.height*s.relativeValue(n[r],o,i)-l.height/2,a;case c.Direction.Down:return a.x=-1*((l.width-u.width)/2+p.left+d.left),a.y=-d.left,a.y+=u.height*s.relativeValue(n[r],o,i)-l.height/2,a;default:return s.assertUnreachable(t)}}))},r.getThumbs=function(){return r.trackRef&&r.trackRef.current?Array.from(r.trackRef.current.children).filter((function(e){return e.hasAttribute("aria-valuenow")})):(console.warn("No thumbs found in the track container. Did you forget to pass & spread the `props` param in renderTrack?"),[])},r.getTargetIndex=function(e){return r.getThumbs().findIndex((function(t){return t===e.target||t.contains(e.target)}))},r.addTouchEvents=function(e){document.addEventListener("touchmove",r.schdOnTouchMove,{passive:!1}),document.addEventListener("touchend",r.schdOnEnd,{passive:!1}),document.addEventListener("touchcancel",r.schdOnEnd,{passive:!1})},r.addMouseEvents=function(e){document.addEventListener("mousemove",r.schdOnMouseMove),document.addEventListener("mouseup",r.schdOnEnd)},r.onMouseDownTrack=function(e){var t;if(0===e.button)if(e.persist(),e.preventDefault(),r.addMouseEvents(e.nativeEvent),r.props.values.length>1&&r.props.draggableTrack){if(r.thumbRefs.some((function(t){var r;return null===(r=t.current)||void 0===r?void 0:r.contains(e.target)})))return;r.setState({draggedTrackPos:[e.clientX,e.clientY]},(function(){return r.onMove(e.clientX,e.clientY)}))}else{var n=s.getClosestThumbIndex(r.thumbRefs.map((function(e){return e.current})),e.clientX,e.clientY,r.props.direction);null===(t=r.thumbRefs[n].current)||void 0===t||t.focus(),r.setState({draggedThumbIndex:n},(function(){return r.onMove(e.clientX,e.clientY)}))}},r.onResize=function(){s.translateThumbs(r.getThumbs(),r.getOffsets(),r.props.rtl),r.calculateMarkOffsets()},r.onTouchStartTrack=function(e){var t;if(e.persist(),r.addTouchEvents(e.nativeEvent),r.props.values.length>1&&r.props.draggableTrack){if(r.thumbRefs.some((function(t){var r;return null===(r=t.current)||void 0===r?void 0:r.contains(e.target)})))return;r.setState({draggedTrackPos:[e.touches[0].clientX,e.touches[0].clientY]},(function(){return r.onMove(e.touches[0].clientX,e.touches[0].clientY)}))}else{var n=s.getClosestThumbIndex(r.thumbRefs.map((function(e){return e.current})),e.touches[0].clientX,e.touches[0].clientY,r.props.direction);null===(t=r.thumbRefs[n].current)||void 0===t||t.focus(),r.setState({draggedThumbIndex:n},(function(){return r.onMove(e.touches[0].clientX,e.touches[0].clientY)}))}},r.onMouseOrTouchStart=function(e){if(!r.props.disabled){var t=s.isTouchEvent(e);if(t||0===e.button){var n=r.getTargetIndex(e);-1!==n&&(t?r.addTouchEvents(e):r.addMouseEvents(e),r.setState({draggedThumbIndex:n,thumbZIndexes:r.state.thumbZIndexes.map((function(e,t){return t===n?Math.max.apply(Math,r.state.thumbZIndexes):e<=r.state.thumbZIndexes[n]?e:e-1}))}))}}},r.onMouseMove=function(e){e.preventDefault(),r.onMove(e.clientX,e.clientY)},r.onTouchMove=function(e){e.preventDefault(),r.onMove(e.touches[0].clientX,e.touches[0].clientY)},r.onKeyDown=function(e){var t=r.props,n=t.values,o=t.onChange,i=t.step,a=t.rtl,c=r.state.isChanged,l=r.getTargetIndex(e.nativeEvent),p=a?-1:1;-1!==l&&(u.includes(e.key)?(e.preventDefault(),r.setState({draggedThumbIndex:l,isChanged:!0}),o(s.replaceAt(n,l,r.normalizeValue(n[l]+p*("PageUp"===e.key?10*i:i),l)))):d.includes(e.key)?(e.preventDefault(),r.setState({draggedThumbIndex:l,isChanged:!0}),o(s.replaceAt(n,l,r.normalizeValue(n[l]-p*("PageDown"===e.key?10*i:i),l)))):"Tab"===e.key?r.setState({draggedThumbIndex:-1},(function(){c&&r.fireOnFinalChange()})):c&&r.fireOnFinalChange())},r.onKeyUp=function(e){var t=r.state.isChanged;r.setState({draggedThumbIndex:-1},(function(){t&&r.fireOnFinalChange()}))},r.onMove=function(e,t){var n=r.state,o=n.draggedThumbIndex,i=n.draggedTrackPos,a=r.props,u=a.direction,d=a.min,l=a.max,p=a.onChange,h=a.values,f=a.step,g=a.rtl;if(-1===o&&-1===i[0]&&-1===i[1])return null;var v=r.trackRef.current;if(!v)return null;var m=v.getBoundingClientRect(),b=s.isVertical(u)?m.height:m.width;if(-1!==i[0]&&-1!==i[1]){var y=e-i[0],w=t-i[1],x=0;switch(u){case c.Direction.Right:case c.Direction.Left:x=y/b*(l-d)+d;break;case c.Direction.Down:case c.Direction.Up:x=w/b*(l-d)+d;break;default:s.assertUnreachable(u)}if(g&&(x*=-1),Math.abs(x)>=f/2){for(var O=0;O<r.thumbRefs.length;O++){if(h[O]===l&&1===Math.sign(x)||h[O]===d&&-1===Math.sign(x))return;var k=h[O]+x;k>l?x=l-h[O]:k<d&&(x=d-h[O])}var T=h.slice(0);for(O=0;O<r.thumbRefs.length;O++)T=s.replaceAt(T,O,r.normalizeValue(h[O]+x,O));r.setState({draggedTrackPos:[e,t]}),p(T)}}else{var M=0;switch(u){case c.Direction.Right:M=(e-m.left)/b*(l-d)+d;break;case c.Direction.Left:M=(b-(e-m.left))/b*(l-d)+d;break;case c.Direction.Down:M=(t-m.top)/b*(l-d)+d;break;case c.Direction.Up:M=(b-(t-m.top))/b*(l-d)+d;break;default:s.assertUnreachable(u)}g&&(M=l+d-M),Math.abs(h[o]-M)>=f/2&&p(s.replaceAt(h,o,r.normalizeValue(M,o)))}},r.normalizeValue=function(e,t){var n=r.props,o=n.min,i=n.max,a=n.step,c=n.allowOverlap,u=n.values;return s.normalizeValue(e,t,o,i,a,c,u)},r.onEnd=function(e){if(e.preventDefault(),document.removeEventListener("mousemove",r.schdOnMouseMove),document.removeEventListener("touchmove",r.schdOnTouchMove),document.removeEventListener("mouseup",r.schdOnEnd),document.removeEventListener("touchend",r.schdOnEnd),document.removeEventListener("touchcancel",r.schdOnEnd),-1===r.state.draggedThumbIndex&&-1===r.state.draggedTrackPos[0]&&-1===r.state.draggedTrackPos[1])return null;r.setState({draggedThumbIndex:-1,draggedTrackPos:[-1,-1]},(function(){r.fireOnFinalChange()}))},r.fireOnFinalChange=function(){r.setState({isChanged:!1});var e=r.props,t=e.onFinalChange,n=e.values;t&&t(n)},r.calculateMarkOffsets=function(){if(r.props.renderMark&&r.trackRef&&null!==r.trackRef.current){for(var e=window.getComputedStyle(r.trackRef.current),t=parseInt(e.width,10),n=parseInt(e.height,10),o=parseInt(e.paddingLeft,10),i=parseInt(e.paddingTop,10),a=[],s=0;s<r.numOfMarks+1;s++){var u=9999,d=9999;if(r.markRefs[s].current){var l=r.markRefs[s].current.getBoundingClientRect();u=l.height,d=l.width}r.props.direction===c.Direction.Left||r.props.direction===c.Direction.Right?a.push([Math.round(t/r.numOfMarks*s+o-d/2),-Math.round((u-n)/2)]):a.push([Math.round(n/r.numOfMarks*s+i-u/2),-Math.round((d-t)/2)])}r.setState({markOffsets:a})}},r.numOfMarks=(t.max-t.min)/r.props.step,r.schdOnMouseMove=s.schd(r.onMouseMove),r.schdOnTouchMove=s.schd(r.onTouchMove),r.schdOnEnd=s.schd(r.onEnd),r.thumbRefs=t.values.map((function(){return a.createRef()}));for(var n=0;n<r.numOfMarks+1;n++)r.markRefs[n]=a.createRef();if(s.isStepDivisible(t.min,t.max,t.step)||console.warn("The difference of `max` and `min` must be divisible by `step`"),0===t.step)throw new Error('"step" property should be a positive number');return r}return n(t,e),t.prototype.componentDidMount=function(){var e=this,t=this.props,r=t.values,n=t.min,o=t.step;this.resizeObserver=window.ResizeObserver?new window.ResizeObserver(this.onResize):{observe:function(){return window.addEventListener("resize",e.onResize)},unobserve:function(){return window.removeEventListener("resize",e.onResize)}},document.addEventListener("touchstart",this.onMouseOrTouchStart,{passive:!1}),document.addEventListener("mousedown",this.onMouseOrTouchStart,{passive:!1}),!this.props.allowOverlap&&s.checkInitialOverlap(this.props.values),this.props.values.forEach((function(t){return s.checkBoundaries(t,e.props.min,e.props.max)})),this.resizeObserver.observe(this.trackRef.current),s.translateThumbs(this.getThumbs(),this.getOffsets(),this.props.rtl),this.calculateMarkOffsets(),r.forEach((function(e){s.isStepDivisible(n,e,o)||console.warn("The `values` property is in conflict with the current `step`, `min`, and `max` properties. Please provide values that are accessible using the min, max, and step values.")}))},t.prototype.componentDidUpdate=function(e){s.translateThumbs(this.getThumbs(),this.getOffsets(),this.props.rtl)},t.prototype.componentWillUnmount=function(){document.removeEventListener("mousedown",this.onMouseOrTouchStart,{passive:!1}),document.removeEventListener("mousemove",this.schdOnMouseMove),document.removeEventListener("touchmove",this.schdOnTouchMove),document.removeEventListener("touchstart",this.onMouseOrTouchStart),document.removeEventListener("mouseup",this.schdOnEnd),document.removeEventListener("touchend",this.schdOnEnd),this.resizeObserver.unobserve(this.trackRef.current)},t.prototype.render=function(){var e=this,t=this.props,r=t.renderTrack,n=t.renderThumb,i=t.renderMark,a=void 0===i?function(){return null}:i,u=t.values,d=t.min,l=t.max,p=t.allowOverlap,h=t.disabled,f=this.state,g=f.draggedThumbIndex,v=f.thumbZIndexes,m=f.markOffsets;return r({props:{style:{transform:"scale(1)",cursor:g>-1?"grabbing":this.props.draggableTrack?s.isVertical(this.props.direction)?"ns-resize":"ew-resize":1!==u.length||h?"inherit":"pointer"},onMouseDown:h?s.voidFn:this.onMouseDownTrack,onTouchStart:h?s.voidFn:this.onTouchStartTrack,ref:this.trackRef},isDragged:this.state.draggedThumbIndex>-1,disabled:h,children:o(m.map((function(t,r){return a({props:{style:e.props.direction===c.Direction.Left||e.props.direction===c.Direction.Right?{position:"absolute",left:t[0]+"px",marginTop:t[1]+"px"}:{position:"absolute",top:t[0]+"px",marginLeft:t[1]+"px"},key:"mark"+r,ref:e.markRefs[r]},index:r})})),u.map((function(t,r){var o=e.state.draggedThumbIndex===r;return n({index:r,value:t,isDragged:o,props:{style:{position:"absolute",zIndex:v[r],cursor:h?"inherit":o?"grabbing":"grab",userSelect:"none",touchAction:"none",WebkitUserSelect:"none",MozUserSelect:"none",msUserSelect:"none"},key:r,tabIndex:h?void 0:0,"aria-valuemax":p?l:u[r+1]||l,"aria-valuemin":p?d:u[r-1]||d,"aria-valuenow":t,draggable:!1,ref:e.thumbRefs[r],role:"slider",onKeyDown:h?s.voidFn:e.onKeyDown,onKeyUp:h?s.voidFn:e.onKeyUp}})})))})},t.defaultProps={step:1,direction:c.Direction.Right,rtl:!1,disabled:!1,allowOverlap:!1,draggableTrack:!1,min:0,max:100},t}(a.Component);t.default=l},3813:function(e,t,r){"use strict";var n=r(0),o=r(3102),i=r(46),a=r(28);function s(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?s(Object(r),!0).forEach((function(t){u(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function u(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var d=Object(a.a)("div",{position:"relative",width:"100%"});d.displayName="Root",d.displayName="StyledRoot";var l=Object(a.a)("div",(function(e){var t=e.$theme,r=e.$value,n=void 0===r?[]:r,o=e.$disabled,i=e.$isDragged,a=t.sizing,s="inherit";return o?s="not-allowed":i?s="grabbing":1===n.length&&(s="pointer"),{paddingTop:a.scale600,paddingBottom:a.scale600,paddingRight:a.scale600,paddingLeft:a.scale600,display:"flex",cursor:s}}));l.displayName="Track",l.displayName="StyledTrack";var p=Object(a.a)("div",(function(e){var t=e.$theme,r=e.$value,n=void 0===r?[]:r,i=e.$min,a=e.$max,s=e.$disabled,c=t.colors,u=t.borders,d=t.direction,l=t.borders.useRoundedCorners?u.radius100:0;return{borderTopLeftRadius:l,borderTopRightRadius:l,borderBottomRightRadius:l,borderBottomLeftRadius:l,background:Object(o.getTrackBackground)({values:n,colors:1===n.length?[s?c.borderOpaque:c.primary,s?c.backgroundSecondary:c.borderOpaque]:[s?c.backgroundSecondary:c.borderOpaque,s?c.borderOpaque:c.primary,s?c.backgroundSecondary:c.borderOpaque],min:i||0,max:a||0,rtl:"rtl"===d}),height:"2px",width:"100%",alignSelf:"center",cursor:s?"not-allowed":"inherit"}}));p.displayName="InnerTrack",p.displayName="StyledInnerTrack";var h=Object(a.a)("div",(function(e){return{width:"4px",height:"2px",backgroundColor:e.$theme.colors.backgroundPrimary,marginLeft:"16px"}}));h.displayName="Mark",h.displayName="StyledMark";var f=Object(a.a)("div",(function(e){return c({},e.$theme.typography.font200,{color:e.$theme.colors.contentPrimary})}));f.displayName="Tick",f.displayName="StyledTick";var g=Object(a.a)("div",(function(e){var t=e.$theme.sizing;return{display:"flex",justifyContent:"space-between",alignItems:"center",paddingRight:t.scale600,paddingLeft:t.scale600,paddingBottom:t.scale400}}));g.displayName="TickBar",g.displayName="StyledTickBar";var v=Object(a.a)("div",(function(e){var t=e.$theme,r=e.$value,n=void 0===r?[]:r,o=e.$thumbIndex,i=e.$disabled,a=2===n.length&&0===o,s=2===n.length&&1===o;return"rtl"===t.direction&&(s||a)&&(a=!a,s=!s),{height:"24px",width:"24px",borderTopLeftRadius:"24px",borderTopRightRadius:"24px",borderBottomLeftRadius:"24px",borderBottomRightRadius:"24px",display:"flex",justifyContent:"center",alignItems:"center",backgroundColor:i?t.colors.contentInverseTertiary:t.colors.contentPrimary,outline:"none",boxShadow:e.$isFocusVisible?"0 0 0 3px ".concat(t.colors.accent):"0 1px 4px rgba(0, 0, 0, 0.12)",cursor:i?"not-allowed":"inherit"}}));v.displayName="Thumb",v.displayName="StyledThumb";var m=Object(a.a)("div",(function(e){return{position:"absolute",top:"-16px",width:"4px",height:"20px",backgroundColor:e.$theme.colors.backgroundInversePrimary}}));m.displayName="InnerThumb",m.displayName="StyledInnerThumb";var b=Object(a.a)("div",(function(e){var t=e.$theme;return c({position:"absolute",top:"-".concat(t.sizing.scale1400)},t.typography.font200,{backgroundColor:t.colors.backgroundInversePrimary,color:t.colors.contentInversePrimary,paddingLeft:t.sizing.scale600,paddingRight:t.sizing.scale600,paddingTop:t.sizing.scale500,paddingBottom:t.sizing.scale500,borderBottomLeftRadius:"48px",borderBottomRightRadius:"48px",borderTopLeftRadius:"48px",borderTopRightRadius:"48px",whiteSpace:"nowrap"})}));b.displayName="ThumbValue",b.displayName="StyledThumbValue";var y=r(18),w=r(182);function x(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function O(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?x(Object(r),!0).forEach((function(t){k(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):x(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function k(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function T(){return(T=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function M(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if(!(Symbol.iterator in Object(e))&&"[object Arguments]"!==Object.prototype.toString.call(e))return;var r=[],n=!0,o=!1,i=void 0;try{for(var a,s=e[Symbol.iterator]();!(n=(a=s.next()).done)&&(r.push(a.value),!t||r.length!==t);n=!0);}catch(c){o=!0,i=c}finally{try{n||null==s.return||s.return()}finally{if(o)throw i}}return r}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}t.a=function(e){var t=e.overrides,r=void 0===t?{}:t,a=e.disabled,s=void 0!==a&&a,c=e.marks,u=void 0!==c&&c,x=e.onChange,k=void 0===x?function(){}:x,R=e.onFinalChange,S=void 0===R?function(){}:R,E=e.min,D=void 0===E?0:E,I=e.max,j=void 0===I?100:I,_=e.step,C=void 0===_?1:_,P=e.value,L=n.useContext(w.a),$=M(n.useState(!1),2),z=$[0],F=$[1],B=M(n.useState(!1),2),A=B[0],N=B[1],V=M(n.useState(!1),2),U=V[0],X=V[1],Y=M(n.useState(-1),2),q=Y[0],K=Y[1],Z=n.useCallback((function(e){Object(i.d)(e)&&X(!0);var t=e.target.parentNode.firstChild===e.target?0:1;K(t)}),[]),J=n.useCallback((function(e){!1!==U&&X(!1),K(-1)}),[]),W=function(e){if(e.length>2||0===e.length)throw new Error("the value prop represents positions of thumbs, so its length can be only one or two");return e}(P),H={$disabled:s,$step:C,$min:D,$max:j,$marks:u,$value:W,$isFocusVisible:U},G=M(Object(y.c)(r.Root,d),2),Q=G[0],ee=G[1],te=M(Object(y.c)(r.Track,l),2),re=te[0],ne=te[1],oe=M(Object(y.c)(r.InnerTrack,p),2),ie=oe[0],ae=oe[1],se=M(Object(y.c)(r.Thumb,v),2),ce=se[0],ue=se[1],de=M(Object(y.c)(r.InnerThumb,m),2),le=de[0],pe=de[1],he=M(Object(y.c)(r.ThumbValue,b),2),fe=he[0],ge=he[1],ve=M(Object(y.c)(r.Tick,f),2),me=ve[0],be=ve[1],ye=M(Object(y.c)(r.TickBar,g),2),we=ye[0],xe=ye[1],Oe=M(Object(y.c)(r.Mark,h),2),ke=Oe[0],Te=Oe[1];return n.createElement(Q,T({"data-baseweb":"slider"},H,ee,{onFocus:Object(i.b)(ee,Z),onBlur:Object(i.a)(ee,J)}),n.createElement(o.Range,T({step:C,min:D,max:j,values:W,disabled:s,onChange:function(e){return k({value:e})},onFinalChange:function(e){return S({value:e})},rtl:"rtl"===L.direction,renderTrack:function(e){var t=e.props,r=e.children,o=e.isDragged;return n.createElement(re,T({onMouseDown:t.onMouseDown,onTouchStart:t.onTouchStart,$isDragged:o},H,ne),n.createElement(ie,T({$isDragged:o,ref:t.ref},H,ae),r))},renderThumb:function(e){var t=e.props,r=e.index,o=e.isDragged,i=(r&&A||!r&&z||o)&&!s;return n.createElement(ce,T({},t,{onMouseEnter:function(){0===r?F(!0):N(!0)},onMouseLeave:function(){0===r?F(!1):N(!1)},$thumbIndex:r,$isDragged:o,style:O({},t.style)},H,ue,{$isFocusVisible:U&&q===r}),i&&n.createElement(fe,T({$thumbIndex:r,$isDragged:o},H,ge),W[r]),i&&n.createElement(le,T({$thumbIndex:r,$isDragged:o},H,pe)))}},u?{renderMark:function(e){var t=e.props;return n.createElement(ke,T({},t,H,Te))}}:{})),n.createElement(we,T({},H,xe),n.createElement(me,T({},H,be),D),n.createElement(me,T({},H,be),j)))}}}]);
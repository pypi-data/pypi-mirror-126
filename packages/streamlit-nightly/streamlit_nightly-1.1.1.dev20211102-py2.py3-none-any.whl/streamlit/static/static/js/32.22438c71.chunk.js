(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[32],{3791:function(e,t,r){"use strict";r.r(t),r.d(t,"default",(function(){return Z}));var o=r(6),i=r(9),n=r(7),a=r(8),l=r(0),c=r.n(l),s=r(37),d=r(18),u=r(28),b=r(86),h=Object.freeze({default:"default",toggle:"toggle",toggle_round:"toggle_round"});Object.freeze({top:"top",right:"right",bottom:"bottom",left:"left"});function m(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function p(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?m(Object(r),!0).forEach((function(t){g(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):m(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function g(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function f(e){var t=e.$disabled,r=e.$checked,o=e.$isIndeterminate,i=e.$isError,n=e.$error,a=e.$isHovered,l=e.$isActive,c=e.$theme,s=e.$checkmarkType===h.toggle,d=c.colors;return t?s?d.sliderTrackFillDisabled:r||o?d.tickFillDisabled:d.tickFill:(n||i)&&(o||r)?l?d.tickFillErrorSelectedHoverActive:a?d.tickFillErrorSelectedHover:d.tickFillErrorSelected:n||i?l?d.tickFillErrorHoverActive:a?d.tickFillErrorHover:d.tickFillError:o||r?l?d.tickFillSelectedHoverActive:a?d.tickFillSelectedHover:d.tickFillSelected:l?s?d.sliderTrackFillActive:d.tickFillActive:a?s?d.sliderTrackFillHover:d.tickFillHover:s?d.sliderTrackFill:d.tickFill}function v(e){var t=e.$disabled,r=e.$theme.colors;return t?r.contentSecondary:r.contentPrimary}var k=Object(u.a)("label",(function(e){var t=e.$disabled,r=e.$labelPlacement;return{flexDirection:"top"===r||"bottom"===r?"column":"row",display:"flex",alignItems:"top"===r||"bottom"===r?"center":"flex-start",cursor:t?"not-allowed":"pointer",userSelect:"none"}}));k.displayName="Root";var $=Object(u.a)("span",(function(e){var t=e.$checked,r=e.$disabled,o=e.$isError,i=e.$error,n=e.$isIndeterminate,a=e.$theme,l=e.$isFocusVisible,c=a.sizing,s=a.animation,d=r?a.colors.tickMarkFillDisabled:o||i?a.colors.tickMarkFillError:a.colors.tickMarkFill,u=encodeURIComponent('\n    <svg width="14" height="4" viewBox="0 0 14 4" fill="none" xmlns="http://www.w3.org/2000/svg">\n      <path d="M14 0.5H0V3.5H14V0.5Z" fill="'.concat(d,'"/>\n    </svg>\n  ')),b=encodeURIComponent('\n    <svg width="17" height="13" viewBox="0 0 17 13" fill="none" xmlns="http://www.w3.org/2000/svg">\n      <path d="M6.50002 12.6L0.400024 6.60002L2.60002 4.40002L6.50002 8.40002L13.9 0.900024L16.1 3.10002L6.50002 12.6Z" fill="'.concat(d,'"/>\n    </svg>\n  ')),h=a.borders.inputBorderRadius,m=function(e){var t=e.$disabled,r=e.$checked,o=e.$isError,i=e.$error,n=e.$isIndeterminate,a=e.$theme,l=e.$isFocusVisible,c=a.colors;return t?c.tickFillDisabled:r||n?"transparent":i||o?c.borderError:l?c.borderSelected:c.tickBorder}(e);return{flex:"0 0 auto",transitionDuration:s.timing200,transitionTimingFunction:s.easeOutCurve,transitionProperty:"background-image, border-color, background-color",width:c.scale700,height:c.scale700,left:"4px",top:"4px",boxSizing:"border-box",borderLeftStyle:"solid",borderRightStyle:"solid",borderTopStyle:"solid",borderBottomStyle:"solid",borderLeftWidth:"3px",borderRightWidth:"3px",borderTopWidth:"3px",borderBottomWidth:"3px",borderLeftColor:m,borderRightColor:m,borderTopColor:m,borderBottomColor:m,borderTopLeftRadius:h,borderTopRightRadius:h,borderBottomRightRadius:h,borderBottomLeftRadius:h,outline:l&&t?"3px solid ".concat(a.colors.accent):"none",display:"inline-block",verticalAlign:"middle",backgroundImage:n?"url('data:image/svg+xml,".concat(u,"');"):t?"url('data:image/svg+xml,".concat(b,"');"):null,backgroundColor:f(e),backgroundRepeat:"no-repeat",backgroundPosition:"center",backgroundSize:"contain",marginTop:a.sizing.scale0,marginBottom:a.sizing.scale0,marginLeft:a.sizing.scale0,marginRight:a.sizing.scale0}}));$.displayName="Checkmark";var y=Object(u.a)("div",(function(e){var t=e.$theme,r=e.$checkmarkType,o=t.typography;return p({flex:r===h.toggle?"auto":null,verticalAlign:"middle"},function(e){var t,r=e.$labelPlacement,o=void 0===r?"":r,i=e.$theme,n=i.sizing.scale300;switch(o){case"top":t="Bottom";break;case"bottom":t="Top";break;case"left":t="Right";break;default:case"right":t="Left"}return"rtl"===i.direction&&"Left"===t?t="Right":"rtl"===i.direction&&"Right"===t&&(t="Left"),g({},"padding".concat(t),n)}(e),{color:v(e)},o.LabelMedium,{lineHeight:"24px"})}));y.displayName="Label";var O=Object(u.a)("input",{opacity:0,width:0,height:0,overflow:"hidden",margin:0,padding:0,position:"absolute"});O.displayName="Input";var w=Object(u.a)("div",(function(e){if(e.$checkmarkType===h.toggle){var t=e.$theme.borders.useRoundedCorners?e.$theme.borders.radius200:null;return p({},Object(b.b)(e.$theme.borders.border300),{alignItems:"center",backgroundColor:e.$theme.colors.mono100,borderTopLeftRadius:t,borderTopRightRadius:t,borderBottomRightRadius:t,borderBottomLeftRadius:t,boxShadow:e.$isFocusVisible?"0 0 0 3px ".concat(e.$theme.colors.accent):e.$theme.lighting.shadow400,outline:"none",display:"flex",justifyContent:"center",height:e.$theme.sizing.scale800,width:e.$theme.sizing.scale800})}if(e.$checkmarkType===h.toggle_round){var r=e.$theme.colors.toggleFill;return e.$disabled?r=e.$theme.colors.toggleFillDisabled:e.$checked&&(e.$error||e.$isError)?r=e.$theme.colors.borderError:e.$checked&&(r=e.$theme.colors.toggleFillChecked),{backgroundColor:r,borderTopLeftRadius:"50%",borderTopRightRadius:"50%",borderBottomRightRadius:"50%",borderBottomLeftRadius:"50%",boxShadow:e.$isFocusVisible?"0 0 0 3px ".concat(e.$theme.colors.accent):e.$isHovered&&!e.$disabled?e.$theme.lighting.shadow500:e.$theme.lighting.shadow400,outline:"none",height:e.$theme.sizing.scale700,width:e.$theme.sizing.scale700,transform:e.$checked?"translateX(".concat("rtl"===e.$theme.direction?"-100%":"100%",")"):null,transition:"transform ".concat(e.$theme.animation.timing200)}}return{}}));w.displayName="Toggle";var R=Object(u.a)("div",(function(e){if(e.$checkmarkType===h.toggle){return{height:e.$theme.sizing.scale300,width:e.$theme.sizing.scale0,borderTopLeftRadius:e.$theme.borders.radius100,borderTopRightRadius:e.$theme.borders.radius100,borderBottomRightRadius:e.$theme.borders.radius100,borderBottomLeftRadius:e.$theme.borders.radius100,backgroundColor:e.$disabled?e.$theme.colors.sliderHandleInnerFillDisabled:e.$isActive&&e.$checked?e.$theme.colors.sliderHandleInnerFillSelectedActive:e.$isHovered&&e.$checked?e.$theme.colors.sliderHandleInnerFillSelectedHover:e.$theme.colors.sliderHandleInnerFill}}return e.$checkmarkType,h.toggle_round,{}}));R.displayName="ToggleInner";var F=Object(u.a)("div",(function(e){if(e.$checkmarkType===h.toggle){var t=e.$theme.borders.useRoundedCorners?e.$theme.borders.radius200:null;return{alignItems:"center",backgroundColor:f(e),borderTopLeftRadius:t,borderTopRightRadius:t,borderBottomRightRadius:t,borderBottomLeftRadius:t,display:"flex",height:e.$theme.sizing.scale600,justifyContent:e.$checked?"flex-end":"flex-start",marginTop:e.$theme.sizing.scale100,marginBottom:e.$theme.sizing.scale100,marginLeft:e.$theme.sizing.scale100,marginRight:e.$theme.sizing.scale100,width:e.$theme.sizing.scale1000}}if(e.$checkmarkType===h.toggle_round){var r=e.$theme.colors.toggleTrackFill;return e.$disabled?r=e.$theme.colors.toggleTrackFillDisabled:(e.$error||e.$isError)&&e.$checked&&(r=e.$theme.colors.tickFillError),{alignItems:"center",backgroundColor:r,borderTopLeftRadius:"7px",borderTopRightRadius:"7px",borderBottomRightRadius:"7px",borderBottomLeftRadius:"7px",display:"flex",height:e.$theme.sizing.scale550,marginTop:e.$theme.sizing.scale200,marginBottom:e.$theme.sizing.scale100,marginLeft:e.$theme.sizing.scale200,marginRight:e.$theme.sizing.scale100,width:e.$theme.sizing.scale1000}}return{}}));F.displayName="ToggleTrack";var j=r(46);function T(e){return(T="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"===typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function x(){return(x=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var o in r)Object.prototype.hasOwnProperty.call(r,o)&&(e[o]=r[o])}return e}).apply(this,arguments)}function C(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function L(e,t){for(var r=0;r<t.length;r++){var o=t[r];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function S(e,t){return!t||"object"!==T(t)&&"function"!==typeof t?E(e):t}function B(e){return(B=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function E(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function P(e,t){return(P=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function M(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var z=function(e){return e.stopPropagation()},H=function(e){function t(){var e,r;C(this,t);for(var o=arguments.length,i=new Array(o),n=0;n<o;n++)i[n]=arguments[n];return M(E(r=S(this,(e=B(t)).call.apply(e,[this].concat(i)))),"state",{isFocused:r.props.autoFocus||!1,isFocusVisible:!1,isHovered:!1,isActive:!1}),M(E(r),"onMouseEnter",(function(e){r.setState({isHovered:!0}),r.props.onMouseEnter(e)})),M(E(r),"onMouseLeave",(function(e){r.setState({isHovered:!1,isActive:!1}),r.props.onMouseLeave(e)})),M(E(r),"onMouseDown",(function(e){r.setState({isActive:!0}),r.props.onMouseDown(e)})),M(E(r),"onMouseUp",(function(e){r.setState({isActive:!1}),r.props.onMouseUp(e)})),M(E(r),"onFocus",(function(e){r.setState({isFocused:!0}),r.props.onFocus(e),Object(j.d)(e)&&r.setState({isFocusVisible:!0})})),M(E(r),"onBlur",(function(e){r.setState({isFocused:!1}),r.props.onBlur(e),!1!==r.state.isFocusVisible&&r.setState({isFocusVisible:!1})})),M(E(r),"isToggle",(function(){return r.props.checkmarkType===h.toggle||r.props.checkmarkType===h.toggle_round})),r}var r,o,i;return function(e,t){if("function"!==typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&P(e,t)}(t,e),r=t,(o=[{key:"componentDidMount",value:function(){var e=this.props,t=e.autoFocus,r=e.inputRef;t&&r.current&&r.current.focus()}},{key:"render",value:function(){var e=this.props.checkmarkType,t=this.props,r=t.overrides,o=void 0===r?{}:r,i=t.onChange,n=t.labelPlacement,a=void 0===n?this.isToggle()?"left":"right":n,c=t.inputRef,s=t.isIndeterminate,u=t.isError,b=t.error,h=t.disabled,m=t.value,p=t.name,g=t.type,f=t.checked,v=t.children,j=t.required,T=t.title,C=t.ariaLabel,L=o.Root,S=o.Checkmark,B=o.Label,E=o.Input,P=o.Toggle,M=o.ToggleInner,H=o.ToggleTrack,V=Object(d.a)(L)||k,I=Object(d.a)(S)||$,D=Object(d.a)(B)||y,A=Object(d.a)(E)||O,U=Object(d.a)(P)||w,_=Object(d.a)(M)||R,W=Object(d.a)(H)||F,N={onChange:i,onFocus:this.onFocus,onBlur:this.onBlur},q={onMouseEnter:this.onMouseEnter,onMouseLeave:this.onMouseLeave,onMouseDown:this.onMouseDown,onMouseUp:this.onMouseUp},J={$isFocused:this.state.isFocused,$isFocusVisible:this.state.isFocusVisible,$isHovered:this.state.isHovered,$isActive:this.state.isActive,$isError:u,$error:b,$checked:f,$isIndeterminate:s,$required:j,$disabled:h,$value:m,$checkmarkType:e},Z=l.createElement(D,x({$labelPlacement:a},J,Object(d.b)(B)),v);return l.createElement(V,x({"data-baseweb":"checkbox",title:T||null,$labelPlacement:a},J,q,Object(d.b)(L)),("top"===a||"left"===a)&&Z,this.isToggle()?l.createElement(W,x({role:"checkbox","aria-checked":s?"mixed":f,"aria-invalid":b||u||null},J,Object(d.b)(H)),l.createElement(U,x({},J,Object(d.b)(P)),l.createElement(_,x({},J,Object(d.b)(M))))):l.createElement(I,x({role:"checkbox",checked:f,"aria-checked":s?"mixed":f,"aria-invalid":b||u||null},J,Object(d.b)(S))),l.createElement(A,x({value:m,name:p,checked:f,required:j,"aria-label":C,"aria-checked":s?"mixed":f,"aria-describedby":this.props["aria-describedby"],"aria-errormessage":this.props["aria-errormessage"],"aria-invalid":b||u||null,"aria-required":j||null,disabled:h,type:g,ref:c,onClick:z},J,N,Object(d.b)(E))),("bottom"===a||"right"===a)&&Z)}}])&&L(r.prototype,o),i&&L(r,i),t}(l.Component);M(H,"defaultProps",{overrides:{},checked:!1,disabled:!1,autoFocus:!1,isIndeterminate:!1,inputRef:l.createRef(),isError:!1,error:!1,type:"checkbox",checkmarkType:h.default,onChange:function(){},onMouseEnter:function(){},onMouseLeave:function(){},onMouseDown:function(){},onMouseUp:function(){},onFocus:function(){},onBlur:function(){}});var V=H,I=r(32),D=r(233),A=r(138),U=r(69),_=r(137),W=r(13),N=r.n(W)()("div",{target:"ek41t0m0"})((function(e){e.theme;return{verticalAlign:"middle",display:"flex",flexDirection:"row",alignItems:"center"}}),""),q=r(5),J=function(e){Object(n.a)(r,e);var t=Object(a.a)(r);function r(){var e;Object(o.a)(this,r);for(var i=arguments.length,n=new Array(i),a=0;a<i;a++)n[a]=arguments[a];return(e=t.call.apply(t,[this].concat(n))).formClearHelper=new D.b,e.state={value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setBoolValue(e.props.element,e.state.value,t)},e.onFormCleared=function(){e.setState({value:e.props.element.default},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.onChange=function(t){var r=t.target.checked;e.setState({value:r},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.render=function(){var t=e.props,r=t.theme,o=t.width,i=t.element,n=t.disabled,a=t.widgetMgr,l=r.colors,c=r.spacing,s=r.radii,d={width:o};return e.formClearHelper.manageFormClearListener(a,i.formId,e.onFormCleared),Object(q.jsx)("div",{className:"row-widget stCheckbox",style:d,children:Object(q.jsx)(V,{checked:e.state.value,disabled:n,onChange:e.onChange,overrides:{Root:{style:function(e){var t=e.$isFocused;return{marginBottom:0,marginTop:0,paddingRight:c.twoThirdsSmFont,backgroundColor:t?l.transparentDarkenedBgMix60:"",borderTopLeftRadius:s.md,borderTopRightRadius:s.md,borderBottomLeftRadius:s.md,borderBottomRightRadius:s.md}}},Checkmark:{style:function(e){var t=e.$isFocusVisible,r=e.$checked,o=r&&!n?l.primary:l.fadedText40;return{outline:0,boxShadow:t&&r?"0 0 0 0.2rem ".concat(Object(I.transparentize)(l.primary,.5)):"",borderLeftWidth:"2px",borderRightWidth:"2px",borderTopWidth:"2px",borderBottomWidth:"2px",borderLeftColor:o,borderRightColor:o,borderTopColor:o,borderBottomColor:o}}},Label:{style:{color:l.bodyText}}},children:Object(q.jsxs)(N,{children:[i.label,i.help&&Object(q.jsx)(_.c,{children:Object(q.jsx)(A.a,{content:i.help,placement:U.b.TOP_RIGHT})})]})})})},e}return Object(i.a)(r,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getBoolValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}}]),r}(c.a.PureComponent),Z=Object(s.withTheme)(J)}}]);
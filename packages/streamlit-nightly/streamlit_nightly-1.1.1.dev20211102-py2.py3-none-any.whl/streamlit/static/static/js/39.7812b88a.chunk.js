(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[39],{3812:function(e,t,n){"use strict";n.r(t),n.d(t,"default",(function(){return h}));var r=n(22),a=n(6),o=n(9),i=n(7),l=n(8),u=n(0),s=n(3761),c=n(233),p=n(137),m=n(138),d=n(69),f=n(5),h=function(e){Object(i.a)(n,e);var t=Object(l.a)(n);function n(){var e;Object(a.a)(this,n);for(var o=arguments.length,i=new Array(o),l=0;l<o;l++)i[l]=arguments[l];return(e=t.call.apply(t,[this].concat(i))).formClearHelper=new c.b,e.state={value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setStringValue(e.props.element,e.state.value,t)},e.onFormCleared=function(){e.setState({value:e.props.element.default},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.handleChange=function(t){var n=e.dateToString(t);e.setState({value:n},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.stringToDate=function(e){var t=e.split(":").map(Number),n=Object(r.a)(t,2),a=n[0],o=n[1],i=new Date;return i.setHours(a),i.setMinutes(o),i},e.dateToString=function(e){var t=e.getHours().toString().padStart(2,"0"),n=e.getMinutes().toString().padStart(2,"0");return"".concat(t,":").concat(n)},e.render=function(){var t=e.props,n=t.disabled,r=t.width,a=t.element,o=t.widgetMgr,i={width:r},l={Select:{props:{disabled:n}}};return e.formClearHelper.manageFormClearListener(o,a.formId,e.onFormCleared),Object(f.jsxs)("div",{className:"stTimeInput",style:i,children:[Object(f.jsx)(p.d,{label:a.label,children:a.help&&Object(f.jsx)(p.b,{children:Object(f.jsx)(m.a,{content:a.help,placement:d.b.TOP_RIGHT})})}),Object(f.jsx)(s.a,{format:"24",value:e.stringToDate(e.state.value),onChange:e.handleChange,overrides:l,creatable:!0})]})},e}return Object(o.a)(n,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getStringValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}}]),n}(u.PureComponent)}}]);
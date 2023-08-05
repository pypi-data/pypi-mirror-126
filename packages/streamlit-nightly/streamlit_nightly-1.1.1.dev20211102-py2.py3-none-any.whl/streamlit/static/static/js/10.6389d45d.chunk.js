/*! For license information please see 10.6389d45d.chunk.js.LICENSE.txt */
(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[10],{2916:function(t,e){},2921:function(t,e){},3215:function(t,e){},3231:function(t,e){},3233:function(t,e){},3260:function(t,e){},3788:function(t,e,n){"use strict";n.r(e),n.d(e,"default",(function(){return B}));var i=n(23),a=n(6),r=n(9),o=n(7),c=n(8),s=n(11),h=n(0),u=n(3656),l=n.n(u),p=n(3157),b=n.n(p),j=n(3158),d=n(2648),f=n(3647),w=n(3014),m=n(3009),O=n(3634),v=n(2649),g=n(188),x=n(10),k=n.n(x),S=n(14),y=n(129),V=n(52),T=n(3774),C=n(213),M=n.n(C),L=n(38),E=function(t){Object(o.a)(n,t);var e=Object(c.a)(n);function n(){return Object(a.a)(this,n),e.apply(this,arguments)}return n}(Object(T.a)(Error)),F=function(t){Object(o.a)(n,t);var e=Object(c.a)(n);function n(){return Object(a.a)(this,n),e.apply(this,arguments)}return n}(Object(T.a)(Error)),N=function(){function t(){Object(a.a)(this,t)}return Object(r.a)(t,null,[{key:"get",value:function(){var e=Object(S.a)(k.a.mark((function e(){var n,i,a;return k.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(n=L.a.current,i=n.commandLine,a=n.userMapboxToken,t.token&&t.commandLine===i.toLowerCase()){e.next=10;break}if(""===a){e.next=6;break}t.token=a,e.next=9;break;case 6:return e.next=8,this.fetchToken("https://data.streamlit.io/tokens.json","mapbox");case 8:t.token=e.sent;case 9:t.commandLine=i.toLowerCase();case 10:return e.abrupt("return",t.token);case 11:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"fetchToken",value:function(){var t=Object(S.a)(k.a.mark((function t(e,n){var i,a;return k.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,M.a.get(e);case 3:if(i=t.sent,null!=(a=i.data[n])&&""!==a){t.next=7;break}throw new Error('Missing token "'.concat(n,'"'));case 7:return t.abrupt("return",a);case 10:throw t.prev=10,t.t0=t.catch(0),new F("".concat(t.t0.message," (").concat(e,")"));case 13:case"end":return t.stop()}}),t,null,[[0,10]])})));return function(e,n){return t.apply(this,arguments)}}()}]),t}();N.token=void 0,N.commandLine=void 0,N.isRunningLocal=function(){var t=window.location.hostname;return"localhost"===t||"127.0.0.1"===t};var D=n(117),J=n.n(D),P=n(130),z=n(5),A=function(t){var e=t.error,n=t.width,i=t.deltaType;return e instanceof E?Object(z.jsx)(P.a,{width:n,name:"No Mapbox token provided",message:Object(z.jsxs)(z.Fragment,{children:[Object(z.jsxs)("p",{children:["To use ",Object(z.jsxs)("code",{children:["st.",i]})," or ",Object(z.jsx)("code",{children:"st.map"})," you need to set up a Mapbox access token."]}),Object(z.jsxs)("p",{children:["To get a token, create an account at"," ",Object(z.jsx)("a",{href:"https://mapbox.com",children:"https://mapbox.com"}),". It's free for moderate usage levels!"]}),Object(z.jsxs)("p",{children:["Once you have a token, just set it using the Streamlit config option ",Object(z.jsx)("code",{children:"mapbox.token"})," and don't forget to restart your Streamlit server at this point if it's still running, then reload this tab."]}),Object(z.jsxs)("p",{children:["See"," ",Object(z.jsx)("a",{href:"https://docs.streamlit.io/library/advanced-features/configuration#view-all-configuration-options",children:"our documentation"})," ","for more info on how to set config options."]})]})}):e instanceof F?Object(z.jsx)(P.a,{width:n,name:"Error fetching Streamlit Mapbox token",message:Object(z.jsxs)(z.Fragment,{children:[Object(z.jsx)("p",{children:"This app requires an internet connection."}),Object(z.jsx)("p",{children:"Please check your connection and try again."}),Object(z.jsxs)("p",{children:["If you think this is a bug, please file bug report"," ",Object(z.jsx)("a",{href:"https://github.com/streamlit/streamlit/issues/new/choose",children:"here"}),"."]})]})}):Object(z.jsx)(P.a,{width:n,name:"Error fetching Streamlit Mapbox token",message:e.message})},I=function(t){return function(e){var n=function(n){Object(o.a)(r,n);var i=Object(c.a)(r);function r(n){var o;return Object(a.a)(this,r),(o=i.call(this,n)).initMapboxToken=Object(S.a)(k.a.mark((function t(){var e;return k.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,N.get();case 3:e=t.sent,o.setState({mapboxToken:e,isFetching:!1}),t.next=10;break;case 7:t.prev=7,t.t0=t.catch(0),o.setState({mapboxTokenError:t.t0,isFetching:!1});case 10:case"end":return t.stop()}}),t,null,[[0,7]])}))),o.render=function(){var n=o.state,i=n.mapboxToken,a=n.mapboxTokenError,r=n.isFetching,c=o.props.width;return a?Object(z.jsx)(A,{width:c,error:a,deltaType:t}):r?Object(z.jsx)(y.a,{body:"Loading...",kind:V.a.INFO,width:c}):Object(z.jsx)(e,Object(s.a)({mapboxToken:i},o.props))},o.state={isFetching:!0,mapboxToken:void 0,mapboxTokenError:void 0},o.initMapboxToken(),o}return r}(h.PureComponent);return n.displayName="withMapboxToken(".concat(e.displayName||e.name,")"),J()(n,e)}},q=n(13),G=n.n(q)()("div",{target:"e1q4dr930"})((function(t){var e=t.width;return{position:"relative",height:t.height,width:e}}),""),R=(n(3206),{classes:Object(s.a)(Object(s.a)(Object(s.a)({},d),m),w)});Object(v.registerLoaders)([O.CSVLoader]);var W=new f.JSONConverter({configuration:R}),_=function(t){Object(o.a)(n,t);var e=Object(c.a)(n);function n(){var t;Object(a.a)(this,n);for(var i=arguments.length,r=new Array(i),o=0;o<i;o++)r[o]=arguments[o];return(t=e.call.apply(e,[this].concat(r))).state={viewState:{bearing:0,pitch:0,zoom:11},initialized:!1,initialViewState:{}},t.componentDidMount=function(){t.setState({initialized:!0})},t.createTooltip=function(e){var n=t.props.element;if(!e||!e.object||!n.tooltip)return!1;var i=JSON.parse(n.tooltip);return i.html?i.html=t.interpolate(e,i.html):i.text=t.interpolate(e,i.text),i},t.interpolate=function(t,e){var n=e.match(/{(.*?)}/g);return n&&n.forEach((function(n){var i=n.substring(1,n.length-1);t.object.hasOwnProperty(i)&&(e=e.replace(n,t.object[i]))})),e},t.onViewStateChange=function(e){var n=e.viewState;t.setState({viewState:n})},t}return Object(r.a)(n,[{key:"render",value:function(){var t=n.getDeckObject(this.props),e=this.state.viewState;return Object(z.jsx)(G,{className:"stDeckGlJsonChart",width:t.initialViewState.width,height:t.initialViewState.height,children:Object(z.jsx)(l.a,{viewState:e,onViewStateChange:this.onViewStateChange,height:t.initialViewState.height,width:t.initialViewState.width,layers:this.state.initialized?t.layers:[],getTooltip:this.createTooltip,controller:!0,children:Object(z.jsx)(j.StaticMap,{height:t.initialViewState.height,width:t.initialViewState.width,mapStyle:t.mapStyle&&("string"===typeof t.mapStyle?t.mapStyle:t.mapStyle[0]),mapboxApiAccessToken:this.props.mapboxToken})})})}}],[{key:"getDerivedStateFromProps",value:function(t,e){var a=n.getDeckObject(t);if(!b()(a.initialViewState,e.initialViewState)){var r=Object.keys(a.initialViewState).reduce((function(t,n){return a.initialViewState[n]===e.initialViewState[n]?t:Object(s.a)(Object(s.a)({},t),{},Object(i.a)({},n,a.initialViewState[n]))}),{});return{viewState:Object(s.a)(Object(s.a)({},e.viewState),r),initialViewState:a.initialViewState}}return null}}]),n}(h.PureComponent);_.getDeckObject=function(t){var e=t.element,n=t.width,i=t.height,a=JSON.parse(e.json);return i?(a.initialViewState.height=i,a.initialViewState.width=n):(a.initialViewState.height||(a.initialViewState.height=500),e.useContainerWidth&&(a.initialViewState.width=n)),delete a.views,W.convert(a)};var B=I("st.pydeck_chart")(Object(g.a)(_))}}]);
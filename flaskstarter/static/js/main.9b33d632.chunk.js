(this.webpackJsonpsite=this.webpackJsonpsite||[]).push([[0],{13:function(t,e,n){},14:function(t,e,n){},15:function(t,e,n){},17:function(t,e,n){"use strict";n.r(e);var o=n(1),s=n.n(o),i=n(8),a=n.n(i),c=(n(13),n(2)),l=n(3),b=n(4),r=n(6),u=n(5),h=n.p+"static/media/logo.6ce24c58.svg",j=(n(14),n(15),n(0)),d=function(t){Object(r.a)(n,t);var e=Object(u.a)(n);function n(){return Object(c.a)(this,n),e.apply(this,arguments)}return Object(l.a)(n,[{key:"render",value:function(){return Object(j.jsx)("h1",{children:"Project"})}}]),n}(o.Component),f=function(t){Object(r.a)(n,t);var e=Object(u.a)(n);function n(t){var o;return Object(c.a)(this,n),(o=e.call(this,t)).state={text:"99 Bottles",bottles:99,bottling:!1,timer:"",button_a:"Next",button_b:"Play"},o.dobottles=o.dobottles.bind(Object(b.a)(o)),o}return Object(l.a)(n,[{key:"componentDidUpdate",value:function(){this.scrollToBottom()}},{key:"scrollToBottom",value:function(){this.el.scrollIntoView({behavior:"smooth"})}},{key:"jsbottles",value:function(t){if(t>0)return"\n".concat((t-=1)+1," bottles of beer on the wall,\n").concat(t+1," bottles of beer.\nTake one down, pass it around.\n").concat(t," bottles of beer on the wall.")}},{key:"dobottles",value:function(){void 0!==this.state.text&&this.state.bottles>0&&this.setState({text:this.state.text+"\n"+this.jsbottles(this.state.bottles),bottles:this.state.bottles-1,bottling:this.state.bottling})}},{key:"render",value:function(){var t=this;return Object(j.jsxs)("header",{className:"App-header",children:[Object(j.jsx)("img",{src:h,className:"App-logo",alt:"logo"}),Object(j.jsx)("h1",{children:"99 Bottles"}),Object(j.jsxs)("div",{children:[Object(j.jsx)("br",{}),Object(j.jsx)("span",{style:{whiteSpace:"pre"},children:this.state.text})]}),Object(j.jsx)("br",{}),Object(j.jsxs)("div",{children:[Object(j.jsxs)("button",{class:"appbutton",onClick:this.dobottles,children:[this.state.button_a," ",this.state.bottles]}),Object(j.jsx)("button",{class:"appbutton",onClick:function(){if(!1===t.state.bottling){var e=setInterval(t.dobottles,2e3);t.setState({bottling:!0,button_b:"Pause",timer:e})}else clearInterval(t.state.timer),t.setState({bottling:!1,timer:"",button_a:"Next",button_b:"Play"})},children:this.state.button_b})]}),Object(j.jsx)("div",{ref:function(e){t.el=e}}),Object(j.jsx)("button",{class:"appbutton",onClick:function(){clearInterval(t.state.timer),t.setState({bottles:99,text:"99 Bottles",bottling:!1,timer:"",button_a:"Next",button_b:"Play"})},children:" Reset "}),Object(j.jsx)(d,{})]})}}]),n}(s.a.Component),p=function(t){t&&t instanceof Function&&n.e(3).then(n.bind(null,18)).then((function(e){var n=e.getCLS,o=e.getFID,s=e.getFCP,i=e.getLCP,a=e.getTTFB;n(t),o(t),s(t),i(t),a(t)}))};a.a.render(Object(j.jsx)(s.a.StrictMode,{children:Object(j.jsx)(f,{})}),document.getElementById("root")),p()}},[[17,1,2]]]);
//# sourceMappingURL=main.9b33d632.chunk.js.map
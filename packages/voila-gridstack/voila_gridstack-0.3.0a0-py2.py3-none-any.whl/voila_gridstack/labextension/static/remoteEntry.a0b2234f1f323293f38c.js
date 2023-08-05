var _JUPYTERLAB;(()=>{"use strict";var e,r,t,a,o,n,i,l,u,d,s,f,p,c,h,b,v,g,y,m,j,w,k={820:(e,r,t)=>{var a={"./index":()=>Promise.all([t.e(379),t.e(43),t.e(810)]).then((()=>()=>t(810))),"./extension":()=>Promise.all([t.e(379),t.e(43),t.e(810)]).then((()=>()=>t(810))),"./style":()=>t.e(186).then((()=>()=>t(186)))},o=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),n=(e,r)=>{if(t.S){var a=t.S.default,o="default";if(a&&a!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[o]=e,t.I(o,r)}};t.d(r,{get:()=>o,init:()=>n})}},S={};function E(e){var r=S[e];if(void 0!==r)return r.exports;var t=S[e]={id:e,exports:{}};return k[e].call(t.exports,t,t.exports,E),t.exports}E.m=k,E.c=S,E.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return E.d(r,{a:r}),r},E.d=(e,r)=>{for(var t in r)E.o(r,t)&&!E.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},E.f={},E.e=e=>Promise.all(Object.keys(E.f).reduce(((r,t)=>(E.f[t](e,r),r)),[])),E.u=e=>e+"."+{43:"5a80814d9222ca08e252",186:"e6c3fd68fcb9d1400a06",379:"64440cb7412bb0528d17",810:"c7247736cec37c95c26c"}[e]+".js?v="+{43:"5a80814d9222ca08e252",186:"e6c3fd68fcb9d1400a06",379:"64440cb7412bb0528d17",810:"c7247736cec37c95c26c"}[e],E.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),E.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="@voila-dashboards/jupyterlab-gridstack:",E.l=(t,a,o,n)=>{if(e[t])e[t].push(a);else{var i,l;if(void 0!==o)for(var u=document.getElementsByTagName("script"),d=0;d<u.length;d++){var s=u[d];if(s.getAttribute("src")==t||s.getAttribute("data-webpack")==r+o){i=s;break}}i||(l=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,E.nc&&i.setAttribute("nonce",E.nc),i.setAttribute("data-webpack",r+o),i.src=t),e[t]=[a];var f=(r,a)=>{i.onerror=i.onload=null,clearTimeout(p);var o=e[t];if(delete e[t],i.parentNode&&i.parentNode.removeChild(i),o&&o.forEach((e=>e(a))),r)return r(a)},p=setTimeout(f.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=f.bind(null,i.onerror),i.onload=f.bind(null,i.onload),l&&document.head.appendChild(i)}},E.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{E.S={};var e={},r={};E.I=(t,a)=>{a||(a=[]);var o=r[t];if(o||(o=r[t]={}),!(a.indexOf(o)>=0)){if(a.push(o),e[t])return e[t];E.o(E.S,t)||(E.S[t]={});var n=E.S[t],i="@voila-dashboards/jupyterlab-gridstack",l=(e,r,t,a)=>{var o=n[e]=n[e]||{},l=o[r];(!l||!l.loaded&&(!a!=!l.eager?a:i>l.from))&&(o[r]={get:t,from:i,eager:!!a})},u=[];return"default"===t&&(l("@voila-dashboards/jupyterlab-gridstack","0.3.0-alpha.0",(()=>Promise.all([E.e(379),E.e(43),E.e(810)]).then((()=>()=>E(810))))),l("gridstack","4.3.1",(()=>E.e(379).then((()=>()=>E(379)))))),e[t]=u.length?Promise.all(u).then((()=>e[t]=1)):1}}})(),(()=>{var e;E.g.importScripts&&(e=E.g.location+"");var r=E.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");t.length&&(e=t[t.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),E.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},a=(e,r)=>{e=t(e),r=t(r);for(var a=0;;){if(a>=e.length)return a<r.length&&"u"!=(typeof r[a])[0];var o=e[a],n=(typeof o)[0];if(a>=r.length)return"u"==n;var i=r[a],l=(typeof i)[0];if(n!=l)return"o"==n&&"n"==l||"s"==l||"u"==n;if("o"!=n&&"u"!=n&&o!=i)return o<i;a++}},o=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var a=1,n=1;n<e.length;n++)a--,t+="u"==(typeof(l=e[n]))[0]?"-":(a>0?".":"")+(a=2,l);return t}var i=[];for(n=1;n<e.length;n++){var l=e[n];i.push(0===l?"not("+u()+")":1===l?"("+u()+" || "+u()+")":2===l?i.pop()+" "+i.pop():o(l))}return u();function u(){return i.pop().replace(/^\((.+)\)$/,"$1")}},n=(e,r)=>{if(0 in e){r=t(r);var a=e[0],o=a<0;o&&(a=-a-1);for(var i=0,l=1,u=!0;;l++,i++){var d,s,f=l<e.length?(typeof e[l])[0]:"";if(i>=r.length||"o"==(s=(typeof(d=r[i]))[0]))return!u||("u"==f?l>a&&!o:""==f!=o);if("u"==s){if(!u||"u"!=f)return!1}else if(u)if(f==s)if(l<=a){if(d!=e[l])return!1}else{if(o?d>e[l]:d<e[l])return!1;d!=e[l]&&(u=!1)}else if("s"!=f&&"n"!=f){if(o||l<=a)return!1;u=!1,l--}else{if(l<=a||s<f!=o)return!1;u=!1}else"s"!=f&&"n"!=f&&(u=!1,l--)}}var p=[],c=p.pop.bind(p);for(i=1;i<e.length;i++){var h=e[i];p.push(1==h?c()|c():2==h?c()&c():h?n(h,r):!c())}return!!c()},i=(e,r)=>{var t=E.S[e];if(!t||!E.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},l=(e,r)=>{var t=e[r];return(r=Object.keys(t).reduce(((e,r)=>!e||a(e,r)?r:e),0))&&t[r]},u=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},d=(e,r,t)=>"Unsatisfied version "+r+" of shared singleton module "+e+" (required "+o(t)+")",s=(e,r,t,a)=>{var o=u(e,t);return n(a,o)||"undefined"!=typeof console&&console.warn&&console.warn(d(t,o,a)),h(e[t][o])},f=(e,r,t)=>{var o=e[r];return(r=Object.keys(o).reduce(((e,r)=>!n(t,r)||e&&!a(e,r)?e:r),0))&&o[r]},p=(e,r,t,a)=>{var n=e[t];return"No satisfying version ("+o(a)+") of shared module "+t+" found in shared scope "+r+".\nAvailable versions: "+Object.keys(n).map((e=>e+" from "+n[e].from)).join(", ")},c=(e,r,t,a)=>{"undefined"!=typeof console&&console.warn&&console.warn(p(e,r,t,a))},h=e=>(e.loaded=1,e.get()),v=(b=e=>function(r,t,a,o){var n=E.I(r);return n&&n.then?n.then(e.bind(e,r,E.S[r],t,a,o)):e(r,E.S[r],t,a,o)})(((e,r,t,a)=>(i(e,t),h(f(r,t,a)||c(r,e,t,a)||l(r,t))))),g=b(((e,r,t,a)=>(i(e,t),s(r,0,t,a)))),y=b(((e,r,t,a,o)=>{var n=r&&E.o(r,t)&&f(r,t,a);return n?h(n):o()})),m={},j={168:()=>g("default","@lumino/signaling",[1,1,4,3]),211:()=>g("default","@lumino/messaging",[1,1,4,3]),249:()=>g("default","@jupyterlab/coreutils",[1,5,2,1]),271:()=>g("default","react",[1,17,0,1]),292:()=>g("default","@jupyter-widgets/jupyterlab-manager",[1,3,0,0]),355:()=>g("default","@jupyterlab/shared-models",[1,3,2,1]),464:()=>g("default","@jupyterlab/mainmenu",[1,3,2,1]),519:()=>v("default","@jupyterlab/cells",[1,3,2,1]),575:()=>g("default","@jupyterlab/notebook",[1,3,2,1]),661:()=>g("default","yjs",[1,13,5,6]),667:()=>y("default","gridstack",[1,4,0,1],(()=>()=>E(379))),677:()=>v("default","@jupyterlab/docregistry",[1,3,2,1]),706:()=>g("default","@lumino/widgets",[1,1,19,0]),728:()=>g("default","@jupyter-widgets/base",[1,4,0,0]),754:()=>g("default","@jupyterlab/rendermime",[1,3,2,1]),766:()=>g("default","@jupyterlab/codeeditor",[1,3,2,1]),797:()=>g("default","@lumino/coreutils",[1,1,5,3]),835:()=>g("default","@jupyterlab/apputils",[1,3,2,1]),850:()=>g("default","@lumino/algorithm",[1,1,3,3]),881:()=>v("default","@jupyterlab/outputarea",[1,3,2,1]),936:()=>g("default","@jupyterlab/ui-components",[1,3,2,1]),938:()=>g("default","@jupyterlab/application",[1,3,2,1])},w={810:[168,211,249,271,292,355,464,519,575,661,667,677,706,728,754,766,797,835,850,881,936,938]},E.f.consumes=(e,r)=>{E.o(w,e)&&w[e].forEach((e=>{if(E.o(m,e))return r.push(m[e]);var t=r=>{m[e]=0,E.m[e]=t=>{delete E.c[e],t.exports=r()}},a=r=>{delete m[e],E.m[e]=t=>{throw delete E.c[e],r}};try{var o=j[e]();o.then?r.push(m[e]=o.then(t).catch(a)):t(o)}catch(e){a(e)}}))},(()=>{var e={699:0};E.f.j=(r,t)=>{var a=E.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else{var o=new Promise(((t,o)=>a=e[r]=[t,o]));t.push(a[2]=o);var n=E.p+E.u(r),i=new Error;E.l(n,(t=>{if(E.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var o=t&&("load"===t.type?"missing":t.type),n=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+o+": "+n+")",i.name="ChunkLoadError",i.type=o,i.request=n,a[1](i)}}),"chunk-"+r,r)}};var r=(r,t)=>{var a,o,[n,i,l]=t,u=0;if(n.some((r=>0!==e[r]))){for(a in i)E.o(i,a)&&(E.m[a]=i[a]);l&&l(E)}for(r&&r(t);u<n.length;u++)o=n[u],E.o(e,o)&&e[o]&&e[o][0](),e[n[u]]=0},t=self.webpackChunk_voila_dashboards_jupyterlab_gridstack=self.webpackChunk_voila_dashboards_jupyterlab_gridstack||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})();var P=E(820);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["@voila-dashboards/jupyterlab-gridstack"]=P})();
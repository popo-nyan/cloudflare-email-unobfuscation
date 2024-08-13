!function () {
    "use strict";

    function e(e) {
        try {
            if ("undefined" == typeof console) {
                return;
            }
            if ("error" in console) {
                console.error(e);
            } else {
                console.log(e);
            }
        } catch (e) {
        }
    }

    function t(e) {
        d.innerHTML = '<a href="' + e.replace(/"/g, "&quot;") + '"></a>';
        return d.childNodes[0].getAttribute("href") || "";
    }

    function r(e, t) {
        var r = e.substr(t, 2);
        return parseInt(r, 16);
    }

    function n(n, c) {
        var o = "";
        var a = r(n, c);
        for (var i = c + 2; i < n.length; i += 2) {
            var l = r(n, i) ^ a;
            o += String.fromCharCode(l);
        }
        try {
            o = decodeURIComponent(escape(o));
        } catch (u) {
            e(u);
        }
        return t(o);
    }

    function c(t) {
        var r = t.querySelectorAll("a");
        for (var c = 0; c < r.length; c++) {
            try {
                var o = r[c];
                var a = o.href.indexOf("/cdn-cgi/l/email-protection#");
                if (a > -1) {
                    o.href = "mailto:" + n(o.href, a + "/cdn-cgi/l/email-protection#".length);
                }
            } catch (i) {
                e(i);
            }
        }
    }

    function o(t) {
        var r = t.querySelectorAll(".__cf_email__");
        for (var c = 0; c < r.length; c++) {
            try {
                var o = r[c];
                var a = o.parentNode;
                var i = o.getAttribute("data-cfemail");
                if (i) {
                    var l = n(i, 0);
                    var d = document.createTextNode(l);
                    a.replaceChild(d, o);
                }
            } catch (h) {
                e(h);
            }
        }
    }

    function a(t) {
        var r = t.querySelectorAll("template");
        for (var n = 0; n < r.length; n++) {
            try {
                i(r[n].content);
            } catch (c) {
                e(c);
            }
        }
    }

    function i(t) {
        try {
            c(t);
            o(t);
            a(t);
        } catch (r) {
            e(r);
        }
    }

    var d = document.createElement("div");
    i(document);
    (function () {
        var e = document.currentScript || document.scripts[document.scripts.length - 1];
        e.parentNode.removeChild(e);
    }());
}();

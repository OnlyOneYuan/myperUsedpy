const CryptoJS = require("crypto-js")

    function undoDes(strName){
        var key = "1876ebf1c532b75e1c16a6f230633c0a";

        var keyHex = CryptoJS.enc.Utf8.parse(key);
        var encrypted = CryptoJS.TripleDES.encrypt(strName, keyHex, {
            iv:CryptoJS.enc.Utf8.parse('83654623'),
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return encrypted.toString()
}
    var uid = function () {
        var i, res = "", len = 32, str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        var strLen = str.length;
        for (i = 0; i < len; i++) {
            res += str.charAt(Math.floor(Math.random() * strLen));
        }
        return res;
};

// 输出代码（命令行调用）
module.exports.init = function (str) {
    console.log(undoDes(str))
}


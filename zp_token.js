/*
@Author: Aloha
@Time: 2024/10/14 15:10
@ProjectName: brandnew
@FileName: zp_token.py
@Software: PyCharm
*/

!'js_code'

function zp_token(s, t) {
    let zp = (new window.ABC).z(s, parseInt(t) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3)
    return encodeURIComponent(zp)
}



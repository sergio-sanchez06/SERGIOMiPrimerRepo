function setCookie(name, value, days, path = '/') {

    let expires = ""
    if (days) {

        const date = new Date()
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000))
        expires = "; expires=" + date.toUTCString()


    }

    document.cookie = name + "=" + (value || "") + expires + "; path=" + path;

}

function getCookie(name){

    const nameEQ = name + "="
    const ca = document.cookie.split(';')

    ca.forEach((c) => {

        while(c.charAt[0] === " ") c = c.substring(1, c.length);
        if(c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);

    })

    return null;

}

function deleteCookie(name, path='/'){

    document.cookie = name + "=; Max-Age=-99999999; path=" + path;

}
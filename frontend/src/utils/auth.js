const tokenVarName = 'token';

export const saveToken = (token, expiry) => {
    document.cookie = `${tokenVarName}=${token}; expires=${expiry} UTC; path=/`;
};

export const deleteToken = () => {
    document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
}

export const getToken = () => {
    let cookies = document.cookie;
    let start = cookies.search(tokenVarName) + tokenVarName.length + 1;
    if (start != -1)
    {
        let end = cookies.indexOf(';', start);
        return cookies.slice(start, end);
    }
    console.log('TOKEN COOKIE NOT FOUND.')
    return null;
};

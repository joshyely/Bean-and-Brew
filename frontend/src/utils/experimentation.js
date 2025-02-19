export const promises = () => {
    const myPromise = new Promise((resolve, reject) => {
        setTimeout(() => {
        resolve("foo");
        }, 300);
    });
  
    myPromise
    .then(handleFulfilledA=>{
        console.log(handleFulfilledA);
    }, handleRejectedA=>{
        console.log(handleRejectedA);
    })
    .then(handleFulfilledB=>{
        console.log(handleFulfilledB);
    }, handleRejectedB=>{
        console.log(handleRejectedB);
    })
    .then(handleFulfilledC=>{
        console.log(handleFulfilledC);
    }, handleRejectedC=>{
        console.log(handleRejectedC);
    });
};

export const uniqueID = () => {
    function naiveId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }
    
    // Generating IDs in a loop
    for (let i = 0; i < 10; i++) {
        let id = naiveId();
        console.log(id);
    }
};

export const playingWithFuncs = () => {
    let now = Date.now();
    let string1 = now.toString(2);
    let string2 = now.toString(5);
    let string3 = now.toString(16);
    let string4 = now.toString(36);
    let string5 = now.toString();
    console.log(now);
    console.log(string1);
    console.log(string2);
    console.log(string3);
    console.log(string4);
    console.log(string5);
    console.log(Math.random().toString(16));
};


export const typeOfExp = (val) => {
    switch(val.constructor){
        case String:
            console.log('value is a string');
            break;
        case Number:
            console.log('value is a number');
            break;
        case Array || Set:
            console.log('value is an array or set');
            break;
    }
};
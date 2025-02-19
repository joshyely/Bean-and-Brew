export const validPattern = (value, pattern) => pattern==null || pattern.test(value);

export const notEmpty = (value) => value.trim() != '' && value != null;

export const sameAs = (value, compare) => {
    if(compare == null){
        return null
    }

    switch(compare.constructor){
        case String || Number || Boolean:
            return value == compare
        case Array:
            for(i of compare){
                if (value != compare) {
                    return false
                }
            }
            return true
        default:
            return null
    }
};

export const differentTo = (value, compare) => {
    if(compare == null){
        return null
    }

    switch(compare.constructor){
        case String || Number || Boolean:
            return value != compare
        case Array:
            for(i of compare){
                if (value == compare) {
                    return false
                }
            }
            return true
        default:
            return null
    }
};



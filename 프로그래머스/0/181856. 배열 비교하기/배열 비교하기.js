function solution(arr1, arr2) {
    if(arr1.length!==arr2.length){
        return arr1.length>arr2.length?1:-1
    }
    else{
        let a1 = arr1.reduce((acc,curr) => acc+curr, 0);
        let a2 = arr2.reduce((acc,curr) => acc+curr, 0);
        return a1>a2?1:a2>a1?-1:0
    }
}
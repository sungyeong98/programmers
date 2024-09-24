function solution(hp) {
    var answer = 0;
    while(hp>0){
        if(hp>=5){
            let temp = Math.floor(hp/5)
            answer+=temp
            hp-=5*temp
        }
        else if(hp>=3){
            let temp = Math.floor(hp/3)
            answer+=temp
            hp-=3*temp
        }
        else{
            let temp = Math.floor(hp/1)
            answer+=temp
            hp-=temp
        }
    }
    return answer;
}
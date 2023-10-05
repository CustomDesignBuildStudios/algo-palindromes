const alphaNumeric = "0123456789abcdefghijklmnopqrstuvwxyz";

function palindrome(inputWord, onlyCheckAlphaNumeric = false) {
    let word = String(inputWord).toLowerCase();

    let newWord = "";
    if(onlyCheckAlphaNumeric){
        for(let i =0;i < word.length;i++){
            if(alphaNumeric.includes(word[i])){
                newWord += word[i];
            }
        }
        word = newWord;
    }

    for(let i =0; i < word.length; i ++){
        console.log(word[i] + " " +word[(word.length-i-1)]);
        if(word[i] != word[(word.length-i-1)]){
            return false;
        }
    }
    return true;
};


module.exports = palindrome;
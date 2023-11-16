function solution(phone_book) {
    phone_book.sort();
    
    for(let i = 0; i < phone_book.length; i++){
        const prefix = phone_book[i];
        
        for(let j = i + 1; j< phone_book.length && phone_book[i].length < phone_book[j].length; j++){
            const string = phone_book[j];
            
            if(string.startsWith(prefix)) return false;
        }
    }

    return true;
}
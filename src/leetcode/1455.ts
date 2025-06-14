// 1455 - Check if a Word Occurs As a Prefix of Any Word in a Sentence

let isPrefixOfWord = function (sentence: string, searchWord: string): number {
  let split_word: string[] = sentence.split(' ');

  for (var i = 0; i < split_word.length; i++) {
    if (split_word[i].startsWith(searchWord)) return i + 1;
  }

  return -1;
}


let isPartOfWord = function (sentence: string, searchWord: string): number[] {
  
  let split_word: string[] = sentence.split(' ');

  let ans: number[] = []

  for (let i = 0; i < split_word.length; i++) {
    if (split_word[i].includes(searchWord, 0)) {
      ans.push(i + 1);
    }
  }

  return ans;
}

let sentence = "this is a test sentences";
let searchWord = "es"

console.log(isPartOfWord(sentence, searchWord));

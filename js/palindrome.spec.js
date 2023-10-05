// Can you translate this driver code to unit tests?

var palindrome = require("./palindrome");

describe("tests palindrome", () => {
    test("palindrome('racecar') === true", () => {
        expect(palindrome('racecar')).toBe(true);
    });
    test("palindrome('Noon') === true", () => {
        expect(palindrome('Noon')).toBe(true);
    });
    test("palindrome('ciVic') === true", () => {
        expect(palindrome('ciVic')).toBe(true);
    });
    test("palindrome('nice') === false", () => {
        expect(palindrome('nice')).toBe(false);
    });
    test("palindrome('A man, a plan, a canal -- Panama') === true", () => {
        expect(palindrome('A man, a plan, a canal -- Panama',true)).toBe(true);
    });
    test("palindrome('Sore was I ere I saw Eros.') === true", () => {
        expect(palindrome('Sore was I ere I saw Eros.',true)).toBe(true);
    });
});
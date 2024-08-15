package main

import (
	"fmt"
	"sort"
	"strings"
	"unicode"
)

func analyzeFrequency(text string, alphabet []rune) map[rune]int {
	frequency := make(map[rune]int)

	for _, letter := range text {
		letter = unicode.ToLower(letter)
		if contains(alphabet, letter) {
			frequency[letter]++
		}
	}

	sortedFrequency := sortFrequency(frequency)
	fmt.Println("\nFrequency of the most common letters:")
	for i, pair := range sortedFrequency {
		if i >= 4 {
			break
		}
		fmt.Printf("Letter: %c, Frequency: %d\n", pair.letter, pair.count)
	}

	return frequency
}

func contains(slice []rune, item rune) bool {
	for _, v := range slice {
		if v == item {
			return true
		}
	}
	return false
}

type letterCount struct {
	letter rune
	count  int
}

func sortFrequency(frequency map[rune]int) []letterCount {
	var sortedFrequency []letterCount
	for k, v := range frequency {
		sortedFrequency = append(sortedFrequency, letterCount{k, v})
	}

	// Sort descending by frequency
	sort.Slice(sortedFrequency, func(i, j int) bool {
		return sortedFrequency[i].count > sortedFrequency[j].count
	})

	return sortedFrequency
}

func calculateShift(frequency map[rune]int, alphabet []rune) int {
	mostFrequentLetter := sortFrequency(frequency)[0].letter
	mostFrequentPosition := indexOf(alphabet, mostFrequentLetter)
	ePosition := indexOf(alphabet, 'e')

	requiredShift := (mostFrequentPosition - ePosition + len(alphabet)) % len(alphabet)
	fmt.Printf("\nShift found for -> ('%c') is: %d\n", mostFrequentLetter, requiredShift)
	return requiredShift
}

func indexOf(slice []rune, item rune) int {
	for i, v := range slice {
		if v == item {
			return i
		}
	}
	return -1
}

func decrypt(text string, shift int, alphabet []rune) string {
	var decryptedText strings.Builder

	for _, letter := range text {
		if contains(alphabet, unicode.ToLower(letter)) {
			newPosition := (indexOf(alphabet, unicode.ToLower(letter)) - shift + len(alphabet)) % len(alphabet)
			if unicode.IsUpper(letter) {
				decryptedText.WriteRune(unicode.ToUpper(alphabet[newPosition]))
			} else {
				decryptedText.WriteRune(alphabet[newPosition])
			}
		} else {
			decryptedText.WriteRune(letter)
		}
	}

	return decryptedText.String()
}

func main() {
	alphabet := []rune("abcdefghijklmnñopqrstuvwxyz")

	encryptedText := `¡"Gnt ebtdtfge wtnpdfme", Pe pw wpxm op wm Gythpdetomo Bmymxpdtñmym. Bpda ¿Cgé etrytqtñm dpmwxpyfp? Xp dpñgpdom xgñsa m Rtadomya Ndgya, cgtpy etpyoa bdtetaypda umxáe ep bpdxtftó epyftdep fmw, bgpe eg pebídtfg k ñayhtññtóy qgpday wtndpe smefm cgp wm xgpdfp wp wtnpdó op eg bdabta ñgpdba, opuáyoa m eg pebídtfg wtnpdmd pw bpyemxtpyfa op wme rpypdmñtaype qgfgdme..."""`

	frequencies := analyzeFrequency(encryptedText, alphabet)
	suggestedShift := calculateShift(frequencies, alphabet)

	fmt.Printf("\nDecrypted text with shift -> (%d):\n\n%s\n", suggestedShift, decrypt(encryptedText, suggestedShift, alphabet))
}

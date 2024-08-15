use std::collections::HashMap;

fn analyze_frequency(text: &str, alphabet: &[char]) -> HashMap<char, usize> {
    let mut frequency: HashMap<char, usize> = HashMap::new();

    for letter in text.chars() {
        let letter = letter.to_lowercase().next().unwrap();
        if alphabet.contains(&letter) {
            *frequency.entry(letter).or_insert(0) += 1;
        }
    }

    let mut sorted_frequency: Vec<(&char, &usize)> = frequency.iter().collect();
    sorted_frequency.sort_by(|a, b| b.1.cmp(a.1));

    println!("\nFrequency of the most common letters:");
    for (_i, (letter, count)) in sorted_frequency.iter().take(4).enumerate() {
        println!("Letter: {}, Frequency: {}", letter, count);
    }

    frequency
}

fn calculate_shift(frequency: &HashMap<char, usize>, alphabet: &[char]) -> usize {
    let most_frequent_letter = *frequency
        .iter()
        .max_by_key(|&(_, count)| count)
        .map(|(letter, _)| letter)
        .unwrap();
    let most_frequent_letter_position = alphabet.iter().position(|&c| c == most_frequent_letter).unwrap();
    let e_position = alphabet.iter().position(|&c| c == 'e').unwrap();

    let required_shift = (most_frequent_letter_position as isize - e_position as isize + alphabet.len() as isize) % alphabet.len() as isize;
    println!("\nShift found for -> ('{}') is: {}", most_frequent_letter, required_shift);

    required_shift as usize
}

fn decrypt(text: &str, shift: usize, alphabet: &[char]) -> String {
    text.chars()
        .map(|letter| {
            let lower_letter = letter.to_lowercase().next().unwrap();
            if alphabet.contains(&lower_letter) {
                let new_position = (alphabet.iter().position(|&c| c == lower_letter).unwrap() as isize - shift as isize + alphabet.len() as isize) % alphabet.len() as isize;
                let decrypted_letter = alphabet[new_position as usize];
                if letter.is_uppercase() {
                    decrypted_letter.to_uppercase().next().unwrap()
                } else {
                    decrypted_letter
                }
            } else {
                letter
            }
        })
        .collect()
}

fn main() {
    let alphabet: Vec<char> = "abcdefghijklmnñopqrstuvwxyz".chars().collect();

    let encrypted_text = r#"¡"Gnt ebtdtfge wtnpdfme", Pe pw wpxm op wm Gythpdetomo Bmymxpdtñmym. Bpda ¿Cgé etrytqtñm dpmwxpyfp? Xp dpñgpdom xgñsa m Rtadomya Ndgya, cgtpy etpyoa bdtetaypda umxáe ep bpdxtftó epyftdep fmw, bgpe eg pebídtfg k ñayhtññtóy qgpday wtndpe smefm cgp wm xgpdfp wp wtnpdó op eg bdabta ñgpdba, opuáyoa m eg pebídtfg wtnpdmd pw bpyemxtpyfa op wme rpypdmñtaype qgfgdme..."""#;

    let frequencies = analyze_frequency(encrypted_text, &alphabet);
    let suggested_shift = calculate_shift(&frequencies, &alphabet);

    println!(
        "\nDecrypted text with shift -> ({}):\n\n{}",
        suggested_shift,
        decrypt(encrypted_text, suggested_shift, &alphabet)
    );
}

require 'set'

alphabet = "abcdefghijklmnñopqrstuvwxyz".chars

def analyze_frequency(text, alphabet)
  frequency = Hash.new(0)
  text.each_char do |letter|
    letter_downcase = letter.downcase
    frequency[letter_downcase] += 1 if alphabet.include?(letter_downcase)
  end

  sorted_frequency = frequency.sort_by { |_letter, count| -count }.to_h
  puts "\nFrequency of the most common letters:"
  sorted_frequency.first(4).each do |letter, count|
    puts "Letter: #{letter}, Frequency: #{count}"
  end
  sorted_frequency
end

def calculate_shift(frequency, alphabet)
  most_frequent_letter = frequency.keys.first
  most_frequent_letter_position = alphabet.index(most_frequent_letter)
  e_position = alphabet.index('e')

  required_shift = (most_frequent_letter_position - e_position) % alphabet.size
  puts "\nShift found for -> ('#{most_frequent_letter}') is: #{required_shift}"
  required_shift
end

def decrypt(text, shift, alphabet)
  text.chars.map do |letter|
    if alphabet.include?(letter.downcase)
      new_position = (alphabet.index(letter.downcase) - shift) % alphabet.size
      letter == letter.upcase ? alphabet[new_position].upcase : alphabet[new_position]
    else
      letter
    end
  end.join
end

encrypted_text = <<-TEXT
¡"Gnt ebtdtfge wtnpdfme", Pe pw wpxm op wm Gythpdetomo Bmymxpdtñmym. Bpda ¿Cgé etrytqtñm dpmwxpyfp? Xp dpñgpdom xgñsa m Rtadomya Ndgya, cgtpy etpyoa bdtetaypda umxáe ep bpdxtftó epyftdep fmw, bgpe eg pebídtfg k ñayhtññtóy qgpday wtndpe smefm cgp wm xgpdfp wp wtnpdó op eg bdabta ñgpdba, opuáyoa m eg pebídtfg wtnpdmd pw bpyemxtpyfa op wme rpypdmñtaype qgfgdme..."""
TEXT

frequencies = analyze_frequency(encrypted_text, alphabet)

suggested_shift = calculate_shift(frequencies, alphabet)

puts "\nDecrypted text with shift -> (#{suggested_shift}):\n\n#{decrypt(encrypted_text, suggested_shift, alphabet)}\n"

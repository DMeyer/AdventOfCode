# Advent Of Code Day 4

import re


class Passport:
    def __init__(self):
        self.byr = ''
        self.iyr = ''
        self.eyr = ''
        self.hgt = ''
        self.hcl = ''
        self.ecl = ''
        self.pid = ''
        self.cid = ''
        self.valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    def isValidPart2(self):
        if self.byr == '' or int(self.byr) < 1920 or int(self.byr) > 2001:
            return False
        if self.iyr == '' or int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return False
        if self.eyr == '' or int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return False

        hgt_match = re.findall("([0-9]+)[in|cm]", self.hgt) 
        if not hgt_match:
            return False
        height = int(hgt_match[0])
        if 'in' in self.hgt and (height < 59 or height > 76):
            return False
        if 'cm' in self.hgt and (height < 150 or height > 193):
            return False

        if not bool(re.search("^#[0-9a-f]{6}$", self.hcl)):
            return False
        
        if self.ecl not in self.valid_ecl:
            return False
        
        if not bool(re.search("^[0-9]{9}$", self.pid)):
            return False

        return True
        
    def isValidPart1(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

    def __repr__(self):
        return f'Passport(byr:{self.byr} iyr:{self.iyr} eyr:{self.eyr} hgt:{self.hgt} hcl:{self.hcl} ecl:{self.ecl} pid:{self.pid} cid:{self.cid})' 

def buildPassports():
    passports = []

    p = Passport()
    for line in open('input'):
        line = line.strip()
        if line == "":
            passports.append(p)
            p = Passport()
        else:
            fields = line.split()

            for f in fields:
                key, value = f.split(':')
                if key == 'byr':
                    p.byr = value
                elif key == 'iyr':
                    p.iyr = value
                elif key == 'eyr':
                    p.eyr = value
                elif key == 'hgt':
                    p.hgt = value
                elif key == 'hcl':
                    p.hcl = value
                elif key == 'ecl':
                    p.ecl = value
                elif key == 'pid':
                    p.pid = value
                elif key == 'cid':
                    p.cid = value
    # The last is not a empty line. This adds the final Passport.
    passports.append(p)
    return passports

def part1(passports):
    valid_passports = 0

    for p in passports:
        if p.isValidPart1():
            valid_passports += 1
    return valid_passports

def part2(passports):
    valid_passports = 0
    
    for p in passports:
        if p.isValidPart2():
            valid_passports += 1
    return valid_passports


passports = buildPassports()

print(f'Day4 Part1 Answer: {part1(passports)}')
print(f'Day4 Part2 Answer: {part2(passports)}')



from credit_card_validator import credit_card_validator
import unittest

class Testcredit_card_validator(unittest.TestCase):

   def test1(self):
      """
      Determine Visa/Mastercard is invalid if it starts with a 0 but meets all other constraints
      Prefix   :  0
      Length   :  16
      Checksum : True
      """
      cc_num = "0000000000000000"
      self.assertFalse(credit_card_validator(cc_num))

   def test2(self):
      """
      Determine card is invalid if it is an empty string
      Length :  0
      """
      cc_num = ""
      self.assertFalse(credit_card_validator(cc_num))

   def test3(self):
      """
      Determine a Visa card is invalid if the prefix is 3 but meets the other constraints
      Prefix   :  3
      Length   :  16
      Checksum :  True
      """
      cc_num = "3"
      self.assertFalse(credit_card_validator(cc_num))

   def test4(self):
      """
      Determine a Visa card number is invalid if it has only 15 digits but meets the other constraints
      Prefix   :  4
      Length   :  15
      Checksum :  True
      """
      cc_num = "4"
      self.assertFalse(credit_card_validator(cc_num))

   def test5(self):
      """
      Determines a Visa card number is invalid using an incorrect checksum value
      Prefix   :  4
      Length   :  16
      Checksum :  False
      """
      cc_num = "4"
      self.assertFalse(credit_card_validator(cc_num))

   def test6(self):
      """
      Determines that a Visa card number is invalid with a length of 17 but meets other constraints
      Prefix   :  4
      Length   :  17
      Checksum :  True
      """
      cc_num = "4"
      self.assertFalse(credit_card_validator(cc_num))

   def test7(self):
      """
      Determines that a Visa card number is invalid with a prefix of 5 but meets other constraints
      Prefix   :  5
      Length   :  16
      Checksum :  True
      """
      cc_num = "5"
      self.assertFalse(credit_card_validator(cc_num))

   def test8(self):
      """
      Determines that a Mastercard number is invalid with a prefix of 50 but meets other constraints
      Prefix   :  50
      Length   :  16
      Checksum :  True
      """
      cc_num = "5"
      self.assertFalse(credit_card_validator(cc_num))

   def test9(self):
      """
      Determines that a Mastercard number is invalid with a length of 15 but meets other constraints
      Prefix   :  51
      Length   :  15
      Checksum :  True
      """
      cc_num = "5"
      self.assertFalse(credit_card_validator(cc_num))

   def test10(self):
      """
      Determines that a Mastercard number is invalid with a bad checksum but meets other constraints
      Prefix   :  51
      Length   :  16
      Checksum :  False
      """
      cc_num = "51"
      self.assertFalse(credit_card_validator(cc_num))

   def test11(self):
      """
      Determines that a Mastercard number is invalid with a length of 17 but meets other constraints
      Prefix   :  51
      Length   :  17
      Checksum :  True
      """
      cc_num = "51"
      self.assertFalse(credit_card_validator(cc_num))

   def test12(self):
      """
      Determines that a Mastercard number is invalid with a length of 15 but meets other constraints
      Prefix   :  55
      Length   :  15
      Checksum :  True
      """
      cc_num = "55"
      self.assertFalse(credit_card_validator(cc_num))

   def test13(self):
      """
      Determines that a Mastercard number is invalid with a bad checksum but meets other constraints
      Prefix   :  55
      Length   :  16
      Checksum :  False
      """
      cc_num = "55"
      self.assertFalse(credit_card_validator(cc_num))

   def test14(self):
      """
      Determines that a Mastercard number is invalid with a length of 17 but meets other constraints
      Prefix   :  55
      Length   :  17
      Checksum :  True
      """
      cc_num = "55"
      self.assertFalse(credit_card_validator(cc_num))

   def test15(self):
      """
      Determines that a Mastercard number is invalid with a prefix of 56 but meets other constraints
      Prefix   :  56
      Length   :  16
      Checksum :  True
      """
      cc_num = "56"
      self.assertFalse(credit_card_validator(cc_num))

   def test16(self):
      """
      Determines that a Mastercard number is invalid with a prefix of 2220 but meets other constraints
      Prefix   :  2220
      Length   :  16
      Checksum :  True
      """
      cc_num = "2220"
      self.assertFalse(credit_card_validator(cc_num))

   def test17(self):
      """
      Determines that a Mastercard number is invalid with a length of 15 but meets other constraints
      Prefix   :  2221
      Length   :  15
      Checksum :  True
      """
      cc_num = "2221"
      self.assertFalse(credit_card_validator(cc_num))

   def test18(self):
      """
      Determines that a Mastercard number is invalid with a bad checksum but meets other constraints
      Prefix   :  2221
      Length   :  16
      Checksum :  False
      """
      cc_num = "2221"
      self.assertFalse(credit_card_validator(cc_num))

   def test19(self):
      """
      Determines that a Mastercard number is invalid with a length of 17 but meets other constraints
      Prefix   :  2221
      Length   :  17
      Checksum :  True
      """
      cc_num = "2221"
      self.assertFalse(credit_card_validator(cc_num))

   def test20(self):
      """
      Determines that a Mastercard number is invalid with a length of 15 but meets other constraints
      Prefix   :  2720
      Length   :  15
      Checksum :  True
      """
      cc_num = "2720"
      self.assertFalse(credit_card_validator(cc_num))

   def test21(self):
      """
      Determines that a Mastercard number is invalid with a bad checksum but meets other constraints
      Prefix   :  2720
      Length   :  16
      Checksum :  False
      """
      cc_num = "2720"
      self.assertFalse(credit_card_validator(cc_num))

   def test22(self):
      """
      Determines that a Mastercard number is invalid with a length of 17 but meets other constraints
      Prefix   :  2720
      Length   :  17
      Checksum :  True
      """
      cc_num = "2720"
      self.assertFalse(credit_card_validator(cc_num))

   def test23(self):
      """
      Determines that a Mastercard number is invalid with a prefix of 2721 but meets other constraints
      Prefix   :  2721
      Length   :  16
      Checksum :  True
      """
      cc_num = "2721"
      self.assertFalse(credit_card_validator(cc_num))

   def test24(self):
      """
      Determines that an Amex card number is invalid with a prefix of 33 but meets other constraints
      Prefix   :  33
      Length   :  16
      Checksum :  True
      """
      cc_num = "33"
      self.assertFalse(credit_card_validator(cc_num))

   def test25(self):
      """
      Determines that an Amex card number is invalid with a length of 14 but meets other constraints
      Prefix   :  34
      Length   :  14
      Checksum :  True
      """
      cc_num = "34"
      self.assertFalse(credit_card_validator(cc_num))

   def test26(self):
      """
      Determines that an Amex card number is invalid with a bad checksum but meets other constraints
      Prefix   :  34
      Length   :  15
      Checksum :  False
      """
      cc_num = "34"
      self.assertFalse(credit_card_validator(cc_num))

   def test27(self):
      """
      Determines that an Amex card number is invalid with a length of 16 but meets other constraints
      Prefix   :  34
      Length   :  16
      Checksum :  True
      """
      cc_num = "34"
      self.assertFalse(credit_card_validator(cc_num))

   def test28(self):
      """
      Determines that an Amex card number is invalid with a prefix of 35 but meets other constraints
      Prefix   :  35
      Length   :  15
      Checksum :  True
      """
      cc_num = "35"
      self.assertFalse(credit_card_validator(cc_num))

   def test29(self):
      """
      Determines that an Amex card number is invalid with a prefix of 36 but meets other constraints
      Prefix   :  36
      Length   :  15
      Checksum :  True
      """
      cc_num = "36"
      self.assertFalse(credit_card_validator(cc_num))

   def test30(self):
      """
      Determines that an Amex card number is invalid with a length of 14 but meets other constraints
      Prefix   :  37
      Length   :  14
      Checksum :  True
      """
      cc_num = "37"
      self.assertFalse(credit_card_validator(cc_num))

   def test31(self):
      """
      Determines that an Amex card number is invalid with a bad checksum but meets other constraints
      Prefix   :  37
      Length   :  15
      Checksum :  False
      """
      cc_num = "37"
      self.assertFalse(credit_card_validator(cc_num))

   def test32(self):
      """
      Determines that an Amex card number is invalid with a length of 16 but meets other constraints
      Prefix   :  37
      Length   :  16
      Checksum :  True
      """
      cc_num = "37"
      self.assertFalse(credit_card_validator(cc_num))

   def test33(self):
      """
      Determines that an Amex card number is invalid with a prefix of 36 but meets other constraints
      Prefix   :  38
      Length   :  15
      Checksum :  True
      """
      cc_num = "38"
      self.assertFalse(credit_card_validator(cc_num))


if __name__ == '__main__':
    unittest.main()
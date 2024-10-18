Feature: Data analysis

  Scenario Outline: Text recognition
    When The text <text> is sent to the server
    Then The functionality <functionID> is executed
    Examples:
      | functionID | text |

  Scenario Outline: Voice recognition
    When The audio <file> is sent to the server
    Then The functionality <functionID> is executed
    Examples:
      | functionID | file |

  Scenario Outline: Tracking
    When The image <file> is sent to the server
    Then The element at (<x>,<y>) is detected
    Examples:
      | x | y | file |

  Scenario Outline: Face recognition
    When The image <file> is sent to the server
    Then The element at (<x>,<y>) is detected
    Examples:
      |  x  |  y  | file         |
      | 281 | 203 | test_01.webp |
      | 293 | 233 | test_02.webp |
      | 342 | 197 | test_03.jpg  |
      | 293 | 221 | test_04.jpg  |
      | 283 | 175 | test_05.webp |
      | 293 | 393 | test_06.jpg  |
      | 260 | 363 | test_07.jpg  |
      | 292 | 262 | test_08.webp |
      | 133 | 156 | test_09.jpg  |
      | 220 | 197 | test_10.webp |
      | 318 | 184 | test_11.jpg  |

  Scenario Outline: Known face recognition
    When The image <file> is sent to the server
    Then The element at (<x>,<y>) is detected
    Examples:
      | x | y | file |

  Scenario Outline: Pose recognition
    When The image <file>, is sent to the server
    Then The element at (<x>,<y>) is detected
    Examples:
      | x | y | file |

  Scenario Outline: Object recognition
    When The image <file> is sent to the server
    Then The element at (<x>,<y>) is detected
    Examples:
      | x | y | file |
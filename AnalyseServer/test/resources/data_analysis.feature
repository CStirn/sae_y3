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
    And The image contains at least one trackable object
    Then The element <target> is detected
    Examples:
      | target | file |

  Scenario Outline: Face recognition
    When The image <file> is sent to the server
    And The image contains at least one face
    Then The element <target> is detected
    Examples:
      | target | file |

  Scenario Outline: Known face recognition
    When The image <file> is sent to the server
    And The image contains at least one face
    And The image contains a known face
    Then The element <target> is detected
    Examples:
      | target | file |

  Scenario Outline: Pose recognition
    When The image <file>, is sent to the server
    And The image contains at least someone doing a known pose
    Then The element <target> is detected
    Examples:
      | target | file |

  Scenario Outline: Object recognition
    When The image <file> is sent to the server
    And The image contains at least one known item
    Then The object <target> is detected
    Examples:
      | target | file |
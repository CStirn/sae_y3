Feature: Fluxes

  Scenario Outline: Recieve from Android device
    When Data <recieved_flux> is sent from an Android device
    Then The data is matching <expected_flux>
    And The data type is detected as <type>
    Examples:
      | type | recieved_flux | expected_flux |

  Scenario Outline: Recieve from iOS device
    When Data <recieved_flux> is sent from an iOS device
    Then The data is matching <expected_flux>
    And The data type is detected as <type>
    Examples:
      | type | recieved_flux | expected_flux |

  Scenario Outline: Recieve from Arduino camera
    When Data <recieved_flux> is sent from an Arduino camera
    Then The data is matching <expected_flux>
    Examples:
      | recieved_flux | expected_flux |

  Scenario Outline: Send infos to the Centralization Server
    When The information <infos> is sent to the Centralization Server
    Then The information was sent correctly
    Examples:
      | infos |

  Scenario Outline: Send files to the Centralization Server
    When The file <file> is sent to the Centralization Server
    Then The file was sent correctly
    Examples:
      | file |

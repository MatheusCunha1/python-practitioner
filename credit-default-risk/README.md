# Credit Scoring - Home Credit Default Risk

Previsão de inadimplência de crédito com base no histórico do cliente, usando o dataset [Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk/data) (Kaggle).

## Modelo de dados

```mermaid
erDiagram
    APPLICATION ||--o{ BUREAU : "SK_ID_CURR"
    BUREAU ||--o{ BUREAU_BALANCE : "SK_ID_BUREAU"
    APPLICATION ||--o{ PREVIOUS_APPLICATION : "SK_ID_CURR"
    PREVIOUS_APPLICATION ||--o{ POS_CASH_BALANCE : "SK_ID_PREV"
    PREVIOUS_APPLICATION ||--o{ INSTALLMENTS_PAYMENTS : "SK_ID_PREV"
    PREVIOUS_APPLICATION ||--o{ CREDIT_CARD_BALANCE : "SK_ID_PREV"
    APPLICATION ||..o{ POS_CASH_BALANCE : "SK_ID_CURR"
    APPLICATION ||..o{ INSTALLMENTS_PAYMENTS : "SK_ID_CURR"
    APPLICATION ||..o{ CREDIT_CARD_BALANCE : "SK_ID_CURR"

    APPLICATION {
        bigint SK_ID_CURR PK
        bigint TARGET
        varchar NAME_CONTRACT_TYPE
        varchar CODE_GENDER
        bigint CNT_CHILDREN
        double AMT_INCOME_TOTAL
        double AMT_CREDIT
        double AMT_ANNUITY
        double AMT_GOODS_PRICE
        varchar NAME_INCOME_TYPE
        varchar NAME_EDUCATION_TYPE
        varchar NAME_FAMILY_STATUS
        bigint DAYS_BIRTH
        bigint DAYS_EMPLOYED
        varchar OCCUPATION_TYPE
        varchar ORGANIZATION_TYPE
        double EXT_SOURCE_1
        double EXT_SOURCE_2
        double EXT_SOURCE_3
    }

    BUREAU {
        bigint SK_ID_BUREAU PK
        bigint SK_ID_CURR FK
        varchar CREDIT_ACTIVE
        varchar CREDIT_CURRENCY
        bigint DAYS_CREDIT
        bigint CREDIT_DAY_OVERDUE
        double DAYS_CREDIT_ENDDATE
        double DAYS_ENDDATE_FACT
        double AMT_CREDIT_MAX_OVERDUE
        bigint CNT_CREDIT_PROLONG
        double AMT_CREDIT_SUM
        double AMT_CREDIT_SUM_DEBT
        double AMT_CREDIT_SUM_LIMIT
        double AMT_CREDIT_SUM_OVERDUE
        varchar CREDIT_TYPE
        bigint DAYS_CREDIT_UPDATE
        double AMT_ANNUITY
    }

    BUREAU_BALANCE {
        bigint SK_ID_BUREAU PK, FK
        bigint MONTHS_BALANCE PK
        varchar STATUS
    }

    PREVIOUS_APPLICATION {
        bigint SK_ID_PREV PK
        bigint SK_ID_CURR FK
        varchar NAME_CONTRACT_TYPE
        double AMT_ANNUITY
        double AMT_APPLICATION
        double AMT_CREDIT
        double AMT_DOWN_PAYMENT
        double AMT_GOODS_PRICE
        varchar NAME_CONTRACT_STATUS
        bigint DAYS_DECISION
        varchar NAME_PAYMENT_TYPE
        varchar CODE_REJECT_REASON
        varchar NAME_CLIENT_TYPE
        varchar NAME_PORTFOLIO
        varchar NAME_PRODUCT_TYPE
        varchar CHANNEL_TYPE
        double CNT_PAYMENT
        varchar NAME_YIELD_GROUP
        varchar PRODUCT_COMBINATION
    }

    POS_CASH_BALANCE {
        bigint SK_ID_PREV PK, FK
        bigint SK_ID_CURR FK
        bigint MONTHS_BALANCE PK
        double CNT_INSTALMENT
        double CNT_INSTALMENT_FUTURE
        varchar NAME_CONTRACT_STATUS
        bigint SK_DPD
        bigint SK_DPD_DEF
    }

    INSTALLMENTS_PAYMENTS {
        bigint SK_ID_PREV FK
        bigint SK_ID_CURR FK
        double NUM_INSTALMENT_VERSION
        bigint NUM_INSTALMENT_NUMBER
        double DAYS_INSTALMENT
        double DAYS_ENTRY_PAYMENT
        double AMT_INSTALMENT
        double AMT_PAYMENT
    }

    CREDIT_CARD_BALANCE {
        bigint SK_ID_PREV PK, FK
        bigint SK_ID_CURR FK
        bigint MONTHS_BALANCE PK
        double AMT_BALANCE
        bigint AMT_CREDIT_LIMIT_ACTUAL
        double AMT_DRAWINGS_ATM_CURRENT
        double AMT_DRAWINGS_CURRENT
        double AMT_DRAWINGS_OTHER_CURRENT
        double AMT_DRAWINGS_POS_CURRENT
        double AMT_INST_MIN_REGULARITY
        double AMT_PAYMENT_CURRENT
        double AMT_PAYMENT_TOTAL_CURRENT
        double AMT_RECEIVABLE_PRINCIPAL
        double AMT_RECIVABLE
        double AMT_TOTAL_RECEIVABLE
        double CNT_DRAWINGS_ATM_CURRENT
        bigint CNT_DRAWINGS_CURRENT
        double CNT_DRAWINGS_OTHER_CURRENT
        double CNT_DRAWINGS_POS_CURRENT
        double CNT_INSTALMENT_MATURE_CUM
        varchar NAME_CONTRACT_STATUS
        bigint SK_DPD
        bigint SK_DPD_DEF
    }
```

Colunas e tipos extraídos de `data/silver`; em `APPLICATION` e `PREVIOUS_APPLICATION` aparecem apenas chaves e colunas principais. Linha pontilhada = relação direta via `SK_ID_CURR`.

const dictionary = {
    ko: {
        messages: {
            email: () => `올바른 이메일 형식이 아닙니다.`,
            required: () => `필수 입력란입니다.`,
            confirmed: (field, confirmedField) => `${confirmedField}와 일치하지 않습니다.`,
            url: () => `올바른 URL 형식이 아닙니다.`
        }
    }
}

export default (Validator) => {
    Validator.Validator.updateDictionary(dictionary)
    Validator.Validator.setLocale('ko')
}

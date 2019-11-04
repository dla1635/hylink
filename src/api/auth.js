/* eslint-disable no-console */
import session from './session';

export default {
    login(email, password) {
        console.log("api", email, password)
        return session.post('/auth/login/', {
            email,
            password
        });
    },
    logout() {
        return session.post('/auth/logout/', {});
    },
    createAccount(email, password1, password2, username) {
        return session.post('/auth/registration/', {
            email,
            password1,
            password2,
            username
        });
    },
    changeAccountPassword(password1, password2) {
        return session.post('/auth/password/change/', {
            password1,
            password2
        });
    },
    sendAccountPasswordResetEmail(email) {
        return session.post('/auth/password/reset/', {
            email
        });
    },
    resetAccountPassword(uid, token, new_password1, new_password2) { // eslint-disable-line camelcase
        return session.post('/auth/password/reset/confirm/', {
            uid,
            token,
            new_password1,
            new_password2
        });
    },
    getAccountDetails() {
        return session.get('/auth/user/');
    },
    updateAccountDetails(data) {
        return session.patch('/auth/user/', data);
    },
    verifyAccountEmail(key) {
        return session.post('/auth/registration/verify-email/', {
            key
        });
    },
};
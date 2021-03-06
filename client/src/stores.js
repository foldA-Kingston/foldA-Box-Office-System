import { writable as persist } from "svelte-persistent-store/session";
// import { writable } from "svelte/store";

export const jwt = persist("jwt", "");
export const emailAddress = persist("emailAddress", "");
export const isAdmin = persist("isAdmin", "");
export const userId = persist("userId", "");

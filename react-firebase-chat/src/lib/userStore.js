import { create } from "zustand";

export const useUserStore = create((set) => ({
  currentUser: null,
  isLoading: true,
  fetchUserInfo: async (uid) => {
    if (!uid) return set({ currentUser: null, isLoading: false });
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/users/${uid}/`);
      if (!response.ok) throw new Error("User not found");

      const data = await response.json();
      set({ currentUser: data, isLoading: false });
    } catch (err) {
      console.log(err);
      set({ currentUser: null, isLoading: false });
    }
  },
}));
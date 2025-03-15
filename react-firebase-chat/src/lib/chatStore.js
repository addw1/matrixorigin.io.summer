import { create } from "zustand";

export const useChatStore = create((set) => ({
  chatId: null,
  user: null,
  isCurrentUserBlocked: false,
  isReceiverBlocked: false,

  changeChat: async (chatId, userId) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/chat/change_chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ chatId, userId }),
      });

      const data = await response.json();
      set(data); // Update Zustand store
    } catch (error) {
      console.error("Error changing chat:", error);
    }
  },

  changeBlock: async (userId) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/chat/toggle_block/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ userId }),
      });

      const data = await response.json();
      set((state) => ({ ...state, isReceiverBlocked: data.isReceiverBlocked }));
    } catch (error) {
      console.error("Error toggling block:", error);
    }
  },

  resetChat: async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/chat/reset_chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      const data = await response.json();
      set(data);
    } catch (error) {
      console.error("Error resetting chat:", error);
    }
  },
}));

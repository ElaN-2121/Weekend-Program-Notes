# Telegram Sender's POV
## 1. Physical Layer (Layer 1)
- **What it does:** Deals with the actual transmission of raw bits (0s and 1s) over a medium.
- **Telegram example:** The internet connection your phone uses—Wi-Fi, mobile data, or Ethernet—so your message can physically travel to Telegram’s servers.

## 2. Data Link Layer (Layer 2)
- When your phone connects to a Wi-Fi router, the router ensures the packets sent from your Telegram app reach it without errors.
## 3. Network Layer (Layer 3)
- **Telegram example:** Your Telegram message is routed through different servers and internet nodes to reach Telegram’s server in the right data center.
## 4. Transport Layer (Layer 4)
- **Telegram example:** Telegram ensures your message (or file) arrives completely and in the correct order. If it’s a voice note, it might use UDP for faster delivery.
## 5. Session Layer (Layer 5)
- **Telegram example:** When you open Telegram and start a chat, a “session” is established between your app and the server, allowing continuous communication.
## 6. Presentation Layer (Layer 6)
- **Telegram example:** Your message text is encrypted before it leaves your device and decrypted by the recipient. If you send a sticker or image, it’s formatted and compressed to save bandwidth.
## 7. Application Layer (Layer 7)
- **Telegram example:** This is the Telegram app itself—where you type messages, send files, view stickers, and interact with chats.

# Telegram Receiver's POV

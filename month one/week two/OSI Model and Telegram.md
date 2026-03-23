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
## 1. Physical Layer (Layer 1) – Signal Reception
- **Telegram example:** Your phone picks up the incoming signals from your router or cell tower that carry your friend’s message.
## 2. Data Link Layer (Layer 2) – Error Checking
- **Telegram example:** Your phone’s network interface confirms that the packet is valid and intact before passing it along. If there’s an error, it can request a resend.
## 3. Network Layer (Layer 3) – Addressing & Routing
- **Telegram example:** Your device identifies that this packet belongs to your Telegram chat, not some other app, using IP addresses.
## 4. Transport Layer (Layer 4) – Reassembly
- **Telegram example:** Your Telegram message, image, or voice note is put back together correctly, so “Hi!” appears exactly as your friend sent it.
## 5. Session Layer (Layer 5) – Managing the Connection
- **Telegram example:** Your app recognizes the message belongs to your active chat session with that friend and maintains continuity.
## 6. Presentation Layer (Layer 6) – Decryption & Formatting
- **Telegram example:** The encrypted message from Telegram’s servers is decrypted, images are decompressed, and stickers or emojis are converted into a readable format.
## 7. Application Layer (Layer 7) – Display
- **Telegram example:** The message “Hi! 😄” appears in your chat interface exactly as your friend sent it. You can now read, react, or reply.
# Summary
Think of **sending** as “packing a message into an envelope and sending it across multiple post offices” and **receiving** as “each post office checking, opening, and passing it along until it reaches your desk.” Every layer has its own role to make sure nothing gets lost, corrupted, or misinterpreted.

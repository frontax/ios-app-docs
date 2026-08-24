# Privacy Policy

## Introduction

This Privacy Policy describes how the iOS app "Climbing Record" (hereinafter "the App") handles user information.
The App respects user privacy and is committed to protecting personal information.

## 1. Information Collected

The App collects the following information:

- Location data (used for GPS tracking and current location sharing)
- Photo library access (used for attaching photos to hike records, auto-detecting past hikes via photo scan, and saving timelapse videos)
- File access (used for importing GPX files, photos, and backup files)
- Microphone access (used for recording voice memos)
- Speech recognition access (used for transcribing voice memos)
- Hiking-related data (mountain name, date/time, elevation, distance, notes, course time plans/actuals, walking pace records, etc.)

## 2. Data Storage

All data is stored exclusively on your device.
No data is transmitted to external servers.
App data is included in device backups (iCloud or Mac/PC), enabling restoration when switching devices.
The database and image files are protected by the device's encryption.
Exported files (GPX, CSV, backup archives) are also protected by device encryption.
Auto-backup data during hikes (GPS track points, session information) is stored in the app's private directory and automatically deleted when the hike is completed or canceled.

## 3. Timelapse Video

The App provides a feature to generate timelapse videos from GPS tracks of hike records.
All video generation processing is performed on-device; GPS track data and generated videos are never transmitted to external servers.
Photo library access permission is required when saving generated videos to the photo library.
Video sharing is executed only when the user explicitly performs a sharing action.

## 4. Location and Course Time Sharing

The App provides a feature to share current location information (latitude, longitude, elevation, map link) during hikes.
Location sharing is executed only when the user explicitly performs a sharing action. The App never automatically transmits location information to third parties.
The course time plan image sharing feature is also executed only when the user explicitly performs a sharing action.
Information handling at the sharing destination is governed by each service's privacy policy.

## 5. Walking Pace Records

The App provides a feature to automatically calculate walking pace (multiplier against standard course time) from past hike records.
All pace calculation processing is performed on-device with no data transmitted to external servers.

## 6. Cache Data

The App stores map tile and network communication cache data on the device to speed up map rendering.
Cache data does not contain user personal information.
Users can check cache data usage and delete it at any time from Settings → Data Management → Cache Management.
Deleting cache does not affect hike records or downloaded offline maps.

## 7. Multilingual Support

The App supports Japanese and English display.
Language switching is automatic based on device system settings; no language setting information is transmitted externally.
Localized display data such as mountain names and prefecture names is entirely contained within the app; no external service communication is performed for translation.

## 8. Statistical Information

The App calculates statistical information from hike records (monthly/yearly hike count, cumulative elevation, walking distance, prefecture-based summit distribution, completion rates for all famous mountain categories, personal records, etc.).
Progress information displayed on highlight cards, such as Hyakumeizan summit rates, is also calculated from on-device hike record data.
All statistical information is calculated and displayed from on-device hike record data and is never transmitted to external servers.

## 9. Course Time Information

The App records and manages course time plans (estimated times and rest periods per checkpoint) and actuals (actual passage times).
All course time calculation processing (time estimation based on trail distance and elevation difference, shortest-path search) is performed on-device.
Real-time reflection of actual times is also processed entirely on-device.
Course time information is stored only on the device and is never transmitted to external servers.

## 10. Photo Handling

Photos saved in the App have their embedded location data (EXIF GPS information) automatically stripped for privacy protection.
Other metadata such as capture date/time is retained.
Photo reordering (drag and drop) in the hike detail screen is processed entirely on-device.
The photo scan feature analyzes location data and capture timestamps of photos in the photo library on-device to auto-detect hike records to famous mountains. This analysis is performed entirely on-device; photo data and location information are never transmitted to external servers. Photos registered as hike records from scan results are saved with location data stripped.

## 11. Voice Memo and Transcription

The App records voice memos during hikes and performs transcription on-device.
Recording data and transcription results are stored exclusively on the device.
Speech recognition prioritizes on-device processing; Apple's speech recognition servers are used only when the device does not support on-device recognition. In that case, audio data is processed in accordance with Apple's Privacy Policy.
Recording data is automatically deleted from the device after transcription is complete.

## 12. AI Features (Highlight Card Caption Generation)

The App uses Apple Intelligence to automatically generate social media captions from hike records.
All AI processing is performed on-device; hike record data is never transmitted to external servers.
Requests (instruction text) entered by users during AI regeneration are also processed only on-device and never transmitted externally.
Generated text is shared only after the user reviews and edits it.
Template-based text generation is used on devices that do not support Apple Intelligence.

## 13. Backup and Restore

Backup files created by the App include hike record data (including course time plans/actuals) and attached images.
Backup files are stored on the device and are not transmitted externally unless the user explicitly performs a sharing action.
Backup files include hash values (SHA-256) for data integrity verification, detecting tampering or corruption during restoration.
Storage and sharing of backup files is the user's responsibility.

## 14. Lock Screen and Dynamic Island Display

The App displays hiking information such as walking distance, elevation, and elapsed time on the Lock Screen and Dynamic Island during hikes (Live Activity feature).
Displayed information is processed on-device and never transmitted to external servers.
The display is automatically cleared when the hike ends or is canceled.

## 15. Links to External Websites

The App provides links to Wikipedia pages for corresponding mountains from the famous mountain detail screen.
Information handling at linked websites is governed by each site's privacy policy.
The App does not transmit user personal information to linked websites.

## 16. In-App Events

The App may offer limited-time in-app events (e.g., Summer Mountain Challenge).
Event period determination and free version record limit changes are all performed on-device with no external server communication.
Badge information awarded in connection with events is also stored only on the device.

## 17. Review Requests

The App may display an App Store review request dialog using iOS standard functionality (StoreKit) when certain conditions are met.
Review request display determination (version, display interval) is performed entirely on-device with no external server communication.
Reviews are submitted through Apple's App Store; the App does not retrieve or store review content.

## 18. Social Media Sharing

Social media sharing of highlight cards, captions, timelapse videos, and course time plan images is executed only when the user explicitly performs a sharing action.
Information handling at the destination social media service is governed by each service's privacy policy.

## 19. Third-Party Disclosure

User personal information is never provided to, sold to, or shared with third parties.

## 20. External Service Communication

The App communicates with the following external services.
No user personal information is transmitted to any of them.

- GSI Tile Server (downloading map tile images)
- GSI Elevation API (obtaining trail elevation profiles)
- Open-Meteo API (obtaining mountain weather forecast data and sunset times)
- Overpass API / OpenStreetMap (searching trail and approach road data)

Communications include the range of the user's location (latitude/longitude range) but do not include device-identifying information or account information.
All communications use HTTPS (encrypted communication).
Communications have a timeout of 15 seconds, preventing unresponsive connections from being maintained for extended periods.

## 21. Audio Output

The App provides audio spoken warnings when deviating from the route.
All audio is generated on-device with no external server communication.

## 22. In-App Purchases

In-app purchases (Pro version) are processed through Apple's payment system.
Payment information (credit card numbers, etc.) is never collected or stored by the App.
Purchase status is securely stored in the device's Keychain (secure storage).

## 23. Data Deletion

Deleting the App from the device removes all stored data (including hike records, course times, source data for statistics, voice memo transcription data, timelapse video temporary data, and cache data).
Individual hike records can also be deleted from within the app.
Deleting a hike record automatically recalculates statistics based on that record.
Cache data can be individually deleted from Settings → Data Management → Cache Management.
Auto-backup data during hikes is deleted upon hike completion, cancellation, or discard in the recovery dialog.
Data exported as backup files must be manually deleted by the user from the Files app or similar.
Timelapse videos saved to the photo library must be manually deleted by the user from the Photos app.

## 24. Changes to This Privacy Policy

This Privacy Policy may be changed without prior notice.
Changes become effective when posted on this page.

**Last Updated:** August 24, 2026

# Actual ChatGPT trial interruption

Surface: assistant-operated Chrome work profile, ChatGPT conversation mode.
Medium (2 of 5) was visibly observed in the model selector; exact model name was not displayed.

CT-01 prepared input was pasted and appeared as an automatically created text attachment.
Upload completion and the enabled Send control were observed. Clicking Send then returned
`Debugger unattached`; no conversation URL, response or successful submission was confirmed.
Do not label CT-01 passed or failed, and do not claim a model rerun. CT-02 through CT-05
were not submitted.

The documented recovery path was attempted: fresh tab inventory, a new ChatGPT tab,
fresh runtime inventory after timeout/reset, and rebinding the inventoried tab. Tab access
again returned `Debugger unattached`. A native Chrome observation through the same CUA
API eventually returned after a prolonged delay (tool reported 21972.7983 seconds), on an
older battery-comparison conversation with disabled composer controls. This did not recover
CT-01 or establish that the current case ran. The root cause remains unknown.

Current gate: five actual responses still unverified; T-0011 remains processing and is not
committed or landed. No browser protection, credential or account setting was changed.
Resume by obtaining a working Chrome control session, then inspect the existing draft or
conversation before sending CT-01 again. Preserve any recovered original response instead
of silently repeating a model run. Existing user approval of T-0005 through T-0014 and the
ChatGPT trial workflow remains valid; do not ask for it again.

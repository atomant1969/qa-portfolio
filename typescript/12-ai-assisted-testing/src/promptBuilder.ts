export function buildBugReportPrompt(notes: string): string {
  // EN: Keep AI output bounded by the evidence supplied by QA.
  // RU: Ограничиваем вывод ИИ только предоставленными QA фактами.
  return `Create a bug report draft using only these notes.
Separate facts from assumptions.

Notes:
${notes}`;
}

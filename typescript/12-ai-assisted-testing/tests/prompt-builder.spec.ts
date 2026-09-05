import { test, expect } from './fixtures';
import { buildBugReportPrompt } from '../src/promptBuilder';

test('bug report prompt includes evidence guardrail', async ({ failureNotes }) => {
  const prompt = buildBugReportPrompt(failureNotes);

  expect(prompt).toContain('using only these notes');
  expect(prompt).toContain('Separate facts from assumptions');
});

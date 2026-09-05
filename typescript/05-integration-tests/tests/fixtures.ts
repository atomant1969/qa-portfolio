import { test as base, expect } from '@playwright/test';

class Repository {
  private records = new Map<string, string>();

  save(id: string, status: string) {
    this.records.set(id, status);
  }

  get(id: string) {
    return this.records.get(id);
  }
}

export const test = base.extend<{ repository: Repository }>({
  repository: async ({}, use) => {
    // EN: Integration fixtures provide shared collaborators for the test.
    // RU: Интеграционные фикстуры предоставляют общие зависимости для теста.
    await use(new Repository());
  },
});

export { expect };

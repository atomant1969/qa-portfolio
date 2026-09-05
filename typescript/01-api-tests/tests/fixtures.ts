import { test as base, expect, type APIResponse } from '@playwright/test';
import http, { type IncomingMessage, type ServerResponse } from 'node:http';

type OrderPayload = {
  customer: string;
  productId: number;
  quantity: number;
};

type Fixtures = {
  apiBaseUrl: string;
  storeApi: {
    login: () => Promise<string>;
    createOrder: (token: string, payload: OrderPayload) => Promise<APIResponse>;
  };
};

export const test = base.extend<Fixtures>({
  apiBaseUrl: async ({}, use) => {
    const server = http.createServer((request: IncomingMessage, response: ServerResponse) => {
      if (request.url === '/api/orders' && request.method === 'POST') {
        const isAuthorized = request.headers.authorization === 'Bearer portfolio-token';
        response.writeHead(isAuthorized ? 201 : 401, { 'content-type': 'application/json' });
        response.end(JSON.stringify(isAuthorized ? { status: 'created' } : { detail: 'Unauthorized' }));
        return;
      }

      response.writeHead(404, { 'content-type': 'application/json' });
      response.end(JSON.stringify({ detail: 'Not found' }));
    });

    await new Promise<void>((resolve) => server.listen(0, resolve));
    const address = server.address();
    if (!address || typeof address === 'string') {
      throw new Error('Local API test server did not start correctly');
    }

    // EN: A local server fixture keeps API tests deterministic and CI-friendly.
    // RU: Локальная фикстура сервера делает API-тесты стабильными для CI.
    await use(`http://127.0.0.1:${address.port}`);
    await new Promise<void>((resolve, reject) => server.close((error) => (error ? reject(error) : resolve())));
  },

  storeApi: async ({ apiBaseUrl, request }, use) => {
    await use({
      async login(): Promise<string> {
        return 'portfolio-token';
      },
      async createOrder(token: string, payload: OrderPayload): Promise<APIResponse> {
        return request.post(`${apiBaseUrl}/api/orders`, {
          data: payload,
          headers: { Authorization: `Bearer ${token}` },
        });
      },
    });
  },
});

export { expect };

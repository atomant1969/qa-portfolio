export type OrderPayload = {
  customer: string;
  productId: number;
  quantity: number;
};

export function generateOrder(index: number): OrderPayload {
  return {
    customer: `Customer ${String(index).padStart(3, '0')}`,
    productId: (index % 3) + 1,
    quantity: (index % 5) + 1,
  };
}

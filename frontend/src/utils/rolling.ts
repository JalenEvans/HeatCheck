export function rolling<T>(arr: T[], window: number): T[][] {
    const result: T[][] = [];
    for (let i = 0; i < arr.length; i++) {
        if (i + 1 >= window) {
            result.push(arr.slice(i + 1 - window, i + 1));
        }
        else {
            result.push([]);
        }
    }

    return result;
}
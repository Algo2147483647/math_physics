async function request(function_name, args_key_value_pairs) {
    const url = 'http://localhost:5000/function';
    try {
        // 创建请求体对象，包含 function 字段和 params 字段
        const requestBody = {
            "function": function_name,
            "params": {}
        };

        // 遍历 args_key_value_pairs 并将键值对添加到 params 字段中
        for (const [key, value] of Object.entries(args_key_value_pairs)) {
            requestBody.params[key] = value;
        }

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // 将包含所有信息的请求体对象转换为 JSON 字符串
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // 解析响应数据
        const responseData = await response.json();
        // 从响应数据中提取 data 字段并解析为 DAG
        const dag = JSON.parse(responseData.data);
        return dag;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
// 梦境杂货铺 API 配置文件
// 你可以在这里修改 API 设置，无需修改主代码

const API_CONFIG = {
    // 图片生成 API
    imageAPI: 'pollinations', // 可选: 'pollinations' (免费), 'gemini' (需要 key)

    // 文字生成 API
    textAPI: 'template', // 可选: 'template' (离线模板), 'gemini' (需要 key)

    // Gemini API Key（如果使用 Gemini 需要填写）
    geminiKey: 'YOUR_GEMINI_API_KEY_HERE',

    // 保底模式：当所有 API 都失败时，使用预设内容
    fallbackMode: true
};

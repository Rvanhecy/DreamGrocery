import re

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义新的 fetchImage 函数
new_function = '''    async function fetchImage(prompt) {
            // 优先尝试 Gemini API（原始代码）
            try {
                const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${apiKey}`;
                const response = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ contents: [{ parts: [{ text: `Pixel art style, high quality cozy dreamcore, soft focus, warm nostalgic colors: ${prompt}` }] }], generationConfig: { responseModalities: ['TEXT', 'IMAGE'] } }) });
                const data = await response.json();

                // 检查响应是否有效
                if (data.candidates && data.candidates[0] && data.candidates[0].content) {
                    return `data:image/png;base64,${data.candidates[0].content.parts.find(p => p.inlineData).inlineData.data}`;
                }
                throw new Error("Gemini API returned invalid response");
            } catch (geminiError) {
                // Gemini API 失败时，自动降级到免费的 Pollinations.ai（保底方案）
                console.warn("Gemini API 不可用，使用保底方案:", geminiError);
                const encodedPrompt = encodeURIComponent(`Pixel art style, high quality cozy dreamcore, soft focus, warm nostalgic colors: ${prompt}`);
                return `https://image.pollinations.ai/prompt/${encodedPrompt}?width=800&height=800&nologo=true`;
            }
        }'''

# 使用正则表达式替换 fetchImage 函数
pattern = r'async function fetchImage\(prompt\) \{[^}]*\{[^}]*\{[^}]*\{[^}]*\{[^}]*\{[^}]*\}[^}]*\}[^}]*\}'
content = re.sub(pattern, new_function.strip(), content, flags=re.DOTALL)

# 写回文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("fetchImage function updated successfully!")
print("- Priority: Gemini API")
print("- Fallback: Pollinations.ai (free)")

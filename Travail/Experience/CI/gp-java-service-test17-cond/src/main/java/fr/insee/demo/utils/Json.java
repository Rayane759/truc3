package fr.insee.demo.utils;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.util.Iterator;

public class Json {
    public static JsonNode mergePreserveMain(JsonNode mainNode, JsonNode updateNode) {
        Iterator<String> fieldNames = updateNode.fieldNames();

        while (fieldNames.hasNext()) {
            String fieldName = fieldNames.next();
            JsonNode mainFieldValue  = mainNode.get(fieldName);
            JsonNode updateFieldValue  = updateNode.get(fieldName);

            // If the node is an embedded object, recurse
            if (mainFieldValue  != null && mainFieldValue .isObject() && updateFieldValue .isObject()) {
                // Both are objects — recurse
                mergePreserveMain(mainFieldValue , updateFieldValue );
            } else  {
                // If main node's field is missing or null, replace it with update's field value
                if (mainFieldValue == null || mainFieldValue.isNull()) {
                    if (mainNode instanceof ObjectNode) {
                        ((ObjectNode) mainNode).set(fieldName, updateFieldValue);
                    }
                }
                // Otherwise keep mainNode's value as is (do nothing)
            }
        }

        return mainNode;
    }
}
